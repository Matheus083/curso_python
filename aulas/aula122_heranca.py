# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Person(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def speak(self):
        print(f'Your NAME is: {self.name} and your LASTNAME is: {self.lastname}')

class Customer(Person):
    ...

class Student(Person):
    ...

c1 = Customer('Matheus', 'Nunes') 
s1 = Student('Lucas', 'Eduardo') 

c1.speak()
s1.speak()

# help(Person)
