from abc import ABC, abstractmethod

class Person(ABC):
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

    @abstractmethod
    def __str__(self):
        pass

class Client(Person):
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self._account = account

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Account: {self.account}"
    