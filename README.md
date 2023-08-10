# ensalamento-umfg

Pequena ferramenta de data-crawling criada para determinar o sexo dos participantes do vestibular da faculdade UMFG com ajuda da API do IBGE.

## Atribuição dos Sexos

A API do IBGE disponibiliza a quantidade de pessoas em que seu sexo foi atribuído a algum nome específico.

Exemplo:
> O nome "Maria" tem, deis de 1930 até 2010, 11.694.738 registros como o sexo feminino, e 39.391 registros com o sexo masculino.

Dado essas quantidades, o sexo foi determinado utilizando a porção com maior quantidade de registros. Utilizando o exemplo anterior como exemplo,
o nome "Maria" tem maior quantidade de registros no sexo feminino, então esse seria atribuído ao nome.

## Resultados

| Curso | Candidatos Totais | do Sexo Feminino | do Sexo Masculino |
|-------|:-----------------:|:----------------:|:-----------------:|
| Administração | 31 | 15 | 16 |
| Agronomia | 48 | 17 | 31 |
| Análise e Desenvolvimento de Sistemas | 88 | 13 | 75 |
| Ciências Contábeis | 17 | 11 | 6 |
| Engenharia Civil | 19 | 7 | 12 |
| Fisioterapia | 31 | 21 | 10 |
| Moda | 12 | 10 | 2 |
| Psicologia | 50 | 42 | 8 |
