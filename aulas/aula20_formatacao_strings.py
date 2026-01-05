"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variable = 'ABC'
print(f'{variable}.')
print(f'{variable:->10}.')  # Espaço à esquerda
print(f'{variable:-<10}.')  # Espaço à direita
print(f'{variable:-^10}.')  # Espaço ao centro
print(f'{1092.374839:.1f}.')  # 1 casa decimal
print(f'{1092.374839:0=+10,.3f}.')  
print(f'The Hexadecimal of 1500 is {1500:08X}')


