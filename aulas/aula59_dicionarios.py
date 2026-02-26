# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

person = {
    'name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'height': 1.75,
    'adresses': [
        {
            'street': 'Main Street',
            'number': 123,
            'city': 'New York',
            'state': 'NY',
            'country': 'USA'
        },
        {
            'street': 'Second Street',
            'number': 456,
            'city': 'Los Angeles',
            'state': 'CA',
            'country': 'USA'
        }
    ]
}

# print(person, type(person))
# print(person['name'])

for key in person:
    print(f'key: {key}, value: {person[key]}')