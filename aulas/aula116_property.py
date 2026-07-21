# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Pen:
    def __init__(self, color):
        self.color_paint = color

    @property
    def color(self):
        print('PROPERTY')
        return self.color_paint
    
    # def get_cor(self):
    #     return self.color
    
pen = Pen('Black')
print(pen.color)