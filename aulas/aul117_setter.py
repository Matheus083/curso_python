# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Pen:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        print('PROPERTY')
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value

pen = Pen('Black')
pen.color = 'Pink'

print(pen.color)

