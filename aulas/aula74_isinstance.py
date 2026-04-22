# Isistance é uma função que verifica se um objeto é uma instância de uma classe ou de uma tupla de classes.

list_1 = ['a', 1, 3.14, True, [1, 2, 3], (1, 2, 3), {'a': 1, 'b': 2}, {0, 1, 2, 3}]

for item in list_1:
    print(f"{item} é uma instância de list: {isinstance(item, list)}")
    print(f"{item} é uma instância de tuple: {isinstance(item, tuple)}")
    print(f"{item} é uma instância de dict: {isinstance(item, dict)}")
    print(f"{item} é uma instância de set: {isinstance(item, set)}")
    print(f"{item} é uma instância de int: {isinstance(item, int)}")
    print(f"{item} é uma instância de float: {isinstance(item, float)}")
    print(f"{item} é uma instância de str: {isinstance(item, str)}")
    print(f"{item} é uma instância de bool: {isinstance(item, bool)}")
    print("-" * 50)

 