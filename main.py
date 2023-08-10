from crawler import CrawlNames
import json

file = open("names-from-pdf.txt", "r")

crawled: CrawlNames

try:
    with open("crawled_data.json", "r") as f:
        crawled = json.loads(f.read())

except FileNotFoundError:
    crawled = CrawlNames(file)

    with open("crawled_data.json", "w") as f:
        f.write(json.dumps(crawled))

candidateCount: dict[str, dict[str, int]] = dict()

for (name, course, sex) in crawled:
    if candidateCount.get(course) is not None:
        candidateCount[course]["total"] += 1
        if sex == "M":
            candidateCount[course]["sexM"] += 1
        else:
            candidateCount[course]["sexF"] += 1
    else:
        candidateCount.setdefault(course, dict(total=0, sexF=0, sexM=0))

ccAsList = list(candidateCount.items())
ccAsList.sort(key=lambda data: data[1]["total"], reverse=True)

sortedCandidateCount = dict(ccAsList)

print(json.dumps(sortedCandidateCount, indent=4, ensure_ascii=False))