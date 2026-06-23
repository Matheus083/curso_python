# # map, partial, GeneratorType e esgotamento de Iterators
from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def increase_percentage(value, percentage):
    return round(value * percentage, 2)

increase_ten_percentage = partial(increase_percentage, percentage=1.1)

def change_price_products(product):
    return {
        **product, 'preco': increase_ten_percentage(product['preco'])
    }

new_products = list(map(change_price_products, products))

print_iter(products)
print_iter(new_products)

print(list(map(lambda x: x * 3, [1, 2, 3, 4])))
