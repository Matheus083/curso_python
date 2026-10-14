class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

class Client(Person):
    def __init__(self, name, age, type_account):
        super().__init__(name, age)
        self._type_account = type_account

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Type Account: {self._type_account}"