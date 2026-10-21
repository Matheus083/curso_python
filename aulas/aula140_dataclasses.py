# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass(init=False)
class Person:
    name: str
    lastname: str

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.full_name = f"{self.name} {self.lastname}"

    # def __post_init__(self):
    #     self.full_name = f"{self.name} {self.lastname}"

    # @property
    # def fullname(self):
    #     return f'{self.name} {self.lastname}'

    # @fullname.setter
    # def fullname(self, value):
    #     name, lastname = value.split(' ')
    #     self.name = name
    #     self.lastname = lastname

if __name__ == '__main__':
    person = Person('John', 'Doe')
    print(person.full_name)
