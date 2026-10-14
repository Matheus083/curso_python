# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()

# directions = enum.Enum('directions', ['LEFT', 'RIGHT'])
# print(directions(1), directions.LEFT, directions['LEFT'])  # directions.LEFT
# print(directions(2).name, directions.RIGHT.value, directions['RIGHT'])  # directions.RIGHT

def move(direction):
    
    if not isinstance(direction, Directions):
        raise ValueError('Invalid direction')
    
    print(f'Moving in the {direction} ({direction.value})')

move(Directions.LEFT)  # Moving in the LEFT
move(Directions.RIGHT)  # Moving in the RIGHT
    