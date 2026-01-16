"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Matheus Nunes.'
other_variable = f'{string[:5]}GOL{string[4:]}'
# string[5] = 'X' # TypeError: 'str' object does not support item assignment
print(other_variable)
print(string.capitalize())
print(string.zfill(50))
