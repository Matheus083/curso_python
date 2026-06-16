# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest
list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    smaller_list = len(l1) if len(l1) < len(l2) else len(l2)
    result = []

    for i in range(smaller_list):
        a = l1[i]
        b = l2[i]
        result.append((a, b))

    return result

test = zipper(list1, list2)
print(test)

def other_zipper(l1, l2):
    return list(zip_longest(l1, l2, fillvalue=None))


test2 = other_zipper(list1, list2)
print()
print(test2)
