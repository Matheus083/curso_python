# Atributos de classe.

class Person:
    YEAR_NOW = 2026

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_Birthday_date(self):
        return Person.YEAR_NOW - self.age
    
p1 = Person('Matheus', 19)
print(p1.get_Birthday_date())

