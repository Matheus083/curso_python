import json

with open('exercicios/exercicio20_json.json', 'r') as file:
    datas_json = json.load(file)

print(json.dumps(datas_json, indent=2, ensure_ascii=False))