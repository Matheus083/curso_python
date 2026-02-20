"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def sum(x, y):
    # definition
    print(f'x={x} + y={y} = {x + y}')

# sum(2, 3)          # argumentos não nomeados
# sum(x=2, y=3)      # argumentos nomeados
# sum(y=3, x=2)      # argumentos nomeados fora de ordem
# sum(2, y=3)        # mistura de argumentos nomeados e não nomeados
# sum(x=2, 3)      # erro: argumento não nomeado após nomeado
sum(2, 7)
