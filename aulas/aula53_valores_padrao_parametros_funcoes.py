"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


def sum(x, y, z=None):
    if z is  not None:
        print(f'{x=} + {y=} + {z=} =', x + y + z)
    else:
        print(f'{x=} + {y=} =', x + y)

sum(1, 2)  # 3
sum(3, 5, 25)
sum(10, 20)
