# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

person = {
    'name': 'Matheus',
    'lastname': 'Nunes'
}

# print(len(person))  # Quantas chaves tem o dicionário
# print(person.keys())  # Iterável com as chaves do dicionário
# print(person.values())  # Iterável com os valores do dicionário
# print(person.items())  # Iterável com as chaves e valores do dicionário
# print(person.setdefault('age', 30))  # Adiciona a chave 'age' com o valor 30 se ela não existir
# print(person)
print(person.get('name'))  # Obtém o valor da chave 'name'
print(person.pop('lastname'))  # Remove a chave 'lastname' e retorna seu valor
print(person)
print(person.popitem())  # Remove o último item adicionado e retorna uma tupla (chave, valor)
print(person)
person.update({'name': 'João', 'age': 25})  # Atualiza o dicionário com os novos valores
print(person)
