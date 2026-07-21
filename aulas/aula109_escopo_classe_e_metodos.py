# Escopo da classe e de metodos da classe.

class Animal:
    def __init__(self, name):
        self.name = name

        variable = 'Value'
        print(variable)

    def eating(self, food='Nothing'):
        return f'{self.name} is eating {food}'

lion = Animal('Lion')

print(lion.name)
print(lion.eating())

