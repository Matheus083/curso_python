# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

import pprint 

def p(v):
    pprint.pprint(v)


array = []
for number in range(10):
    array.append(number)

# print(array)

# print()

array_2 = [number * 2 for number in range(10)]
# print(array_2)

# Mapeamento de dados com list comprehension.

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

new_products = [{**number, 'preco': number['preco']  * 1.5 } if number['preco'] > 15 else {**number} for number in produtos  if number['preco'] > 15]
# p(new_products)

# new_list = [n for n in range(10) if n < 5]
# print(new_list) 

p(new_products)
