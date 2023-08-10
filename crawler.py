import re
from io import TextIOWrapper
from typing import Literal
import requests
from functools import reduce

class CrawlNames(list[tuple[str, str, str]]):
    # 000.0XX.XXX-XX
    NAME_EXP = re.compile("^.*\\d{3}\\.\\dXX\\.XXX-XX$", re.MULTILINE)

    COURSES = [
        "Administração",
        "Agronomia",
        "Análise e Desenvolvimento de Sistemas",
        "Ciências Contábeis",
        "Engenharia Civil",
        "Fisioterapia",
        "Moda",
        "Psicologia"
    ]
    courses: list[str]

    def __init__(self, file: TextIOWrapper, courses: list[str] | None = None):
        super().__init__()

        if courses is None:
            self.courses = self.COURSES
        else:
            self.courses = courses

        text = file.read()
        nameLines: list[str] = self.NAME_EXP.findall(text)

        for line in nameLines:
            pair = self._mapNamesByCourses(line)
            sex = self._getSex(pair[0].split(" ")[0])
            self.append((*pair, sex))

    def _mapNamesByCourses(self, line: str):
        for course in self.courses:
            if course in line:
                components = line.split(course)
                return (components[0].strip(), course)
        raise Exception(f'No course found for line "{line}"')

    def _getSex(self, firstName: str) -> Literal["M", "F"]:
        sexF = requests.get(f"http://servicodados.ibge.gov.br/api/v2/censos/nomes/{firstName}?sexo=F")
        sexM = requests.get(f"http://servicodados.ibge.gov.br/api/v2/censos/nomes/{firstName}?sexo=M")

        sexFjson = sexF.json()
        sexMjson = sexM.json()

        if len(sexFjson) == 0:
            return "M"
        if len(sexMjson) == 0:
            return "F"

        resultF = sexFjson[0]
        resultM = sexMjson[0]

        countsF = list(map(lambda d: d["frequencia"], resultF["res"]))
        countsM = list(map(lambda d: d["frequencia"], resultM["res"]))

        totalF = reduce((lambda acc, n: acc + n), countsF, 0)
        totalM = reduce((lambda acc, n: acc + n), countsM, 0)

        if totalF > totalM:
            return "F"
        return "M"