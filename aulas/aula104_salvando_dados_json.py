import json 

# person = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aulas/aula104.json', 'w') as file:
#     json.dump(person, file, ensure_ascii=False, indent=2)

with open('aulas/aula104.json', 'r', encoding='utf8') as file:
    person = json.load(file)
    print(person)
    print(person['nome'])
