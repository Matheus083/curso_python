# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

persons = ['Maria', 'João', 'Luiz', 'Ana']
shirt = [['Preta', 'Branca'], ['M', 'G'], ['Mens', 'Womens', 'Unisex'], ['Coton', 'Polyester']]

combination = combinations(persons, 2)
print(*list(combination), sep='\n')

print()

permutation = permutations(persons, 2)
print(*list(permutation), sep='\n')

print()

products = product(*shirt)
print(*list(products), sep='\n')
