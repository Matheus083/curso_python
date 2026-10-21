class Person():
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

class Client(Person):
    def __init__(self, name: str, age: int, account: int | None) -> None:
        super().__init__(name, age)
        self._account = account

    @property
    def account(self) -> int:
        return self._account

    @account.setter
    def account(self, account: int) -> None:
        self._account = account

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Account: {self.account}"
