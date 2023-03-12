import json
import re
import csv

def leitura():
    jsonArray = []

    with open("alunos.csv", encoding = 'utf-8') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            new_row = {}
            for key, value in row.items():
                if "{" in key:
                    match = re.match(r'^(\w+)\{(.+?)\}(::sum|::media)?$',key)
                    if match:
                        head, indices, func = match.groups()
                        indices = list(map(int, indices.split(",")))
                        if func == "::sum":
                            row[head+"_sum"] = sum([int(value.split(",")[i-1]) for i in indices])
                        elif func == "::media":
                            row[head+"_media"] = sum([int(value.split(",")[i-1]) for i in indices]) / len(indices)
                new_row[key] = value
            jsonArray.append(row)
    return jsonArray

print(leitura())