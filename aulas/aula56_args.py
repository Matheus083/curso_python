"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento


# x, y, *rest = 1, 2, 3, 4
# print(x, y, rest)
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def sum_args(*args):
    total = 0
    for n in args:
        total += n
    return total

sum_numbers = sum_args(17, 25,3, 99,66,54, 57,101,109, 88, 45, 23, 12, 34, 56, 78, 90)
print(sum_numbers)
