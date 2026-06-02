# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtcs = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# ex1.:
new_products = copy.deepcopy(produtcs)
list_comprehension = [{**prod, 'preco': round(prod['preco'] * 1.1, 2)} for prod in new_products]


# ex2.:
sorted_list = sorted(list_comprehension, key=lambda product: product['nome'], reverse=True)
# print(*sorted_list, sep='\n')

# exe3.:
sorted_list2 = sorted(list_comprehension, key=lambda product: product['preco'])
print(*sorted_list2, sep='\n')
