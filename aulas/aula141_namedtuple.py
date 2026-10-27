# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple
from collections import namedtuple
from typing import NamedTuple

class Card(NamedTuple):
    value: str = 'VALUE'
    suit:  str = 'SUIT'

# Card = namedtuple('Card', ['value', 'suit'], defaults=['VALUE', 'SUIT'])
as_swords = Card('A', '🂡')


# print(as_swords)
# print(as_swords.suit)
# print(as_swords.value)
print(as_swords._field_defaults)

# for itens in as_swords:
#     print(itens)