# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

array = []
for number in range(10):
    array.append(number)

print(array)

print()

array_2 = [number * 2 for number in range(10)]
print(array_2)

