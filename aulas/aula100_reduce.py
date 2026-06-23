# reduce - faz a redução de um iterável em um valor.
from functools import reduce

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

"""
Lógica da função:
def function_reduce(count, product):
    print('Count: ', count)
    print('Product', product)
    print()
    return count + product['preco]

total = 0
for p in products:
    total += p['preco']

print(total)

print(sum([p['preco'] for p in products]))
"""

new_products = reduce(lambda ac, p: ac + p['preco'], products, 0)

print("The total is: ", new_products)
