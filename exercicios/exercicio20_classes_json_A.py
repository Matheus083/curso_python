# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class Person:
    def __init__(self, name=None, age=None, data_birthday=None, height=None):
        self.name = name
        self.age = age
        self.data_birthday = data_birthday
        self.height = height

    def info(self):
        return f' NAME: {self.name} \n AGE: {self.age} \n DATA_BIRTHDAY: {self.data_birthday} \n HEIGHT: {self.height} \n'
    
p1 = Person('Matheus', 19, 2007, 1.84)
p2 = Person('Beatriz', 15, 2011, 1.60)

# print(vars(p1))
# print(vars(p2))
# print(p1.info())

with open('exercicios/exercicio20_json.json', 'w') as file:
    json.dump((vars(p1), vars(p2)), file, ensure_ascii=False, indent=2)

