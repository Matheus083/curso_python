# __dict__ e vars para atributos de instancia.
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_Birthday_date(self):
        return Person.YEAR_NOW - self.age\
    
p1 = Person('Matheus', 35)

p1.__dict__['other'] = 'Null'
print(p1.__dict__)
print(vars(p1))


