# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Person:
    year = 2026
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def method_class(cls):
        print('Hey')

    @classmethod
    def create_with_50(cls, name):
        return cls(name, 50)

print(Person.year)

p1 = Person('Matheus', 19)
p1.method_class()
p2 = Person.create_with_50('Matheus')
Person.method_class()

print(p2.name, p2.age)