# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname 

p1 = Person('Matheus', 'Nunes')

print(p1.name)
print(p1.lastname)

