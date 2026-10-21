from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: int, account_number: int):
        self.__agency = agency
        self.__account_number = account_number
        self._balance = 0

    @abstractmethod
    def withdraw(self, value: float) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    def agency(self) -> int:
        return self.__agency

    @agency.setter
    def agency(self, value: int) -> None:
        self.__agency = value
    
    @property
    def account_number(self) -> int:
        return self.__account_number

    @account_number.setter
    def account_number(self, value: int) -> None:
        self.__account_number = value

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        self._balance = value

    def deposit(self, value: float) -> float:
        try:
            if value <= 0:
                raise ValueError("The value must be a number greater than zero.")
            self._balance += value
            return self._balance
        except ValueError as e:
            print(f"(ERROR) - {e}")
            e.add_note("The value must be a number.")
            return self._balance

class CurrentAccount(Account):
    def __init__(self, agency: int, account_number: int) -> None:
        super().__init__(agency, account_number)
        self._limit = 200 

    def withdraw(self, value: float) -> float:
        try:
            if value <= 0 or value == 0:
                raise ValueError("The value must be a number greater than zero.")
            
            if value <= self._balance:
                self._balance -= value
                return self._balance

            if value <= self._balance + self._limit:
                print("(WARNING) - Withdrawing with limit.")
                self._balance -= value
                self._limit -= value / 2
                return self._balance

            print("(WARNING) - Not enough balance.")
            return self._balance
        
        except ValueError as e:
            print(f"(ERROR) - {e}")
            e.add_note("The value must be a number or you can't withdraw more than the balance + limit.")
            return self._balance
        
    def __str__(self):
        return f"Agency: {self.agency}, Account Number: {self.account_number}, Balance: {self._balance}, Limit: {self._limit}"
    
class SavingsAccount(Account):
    def __init__(self, agency: int, account_number: int) -> None:
        super().__init__(agency, account_number)

    def withdraw(self, value: float) -> float:
        try:
            if value <= 0 or value == 0:
                raise ValueError("The value must be a number greater than zero.")
            
            if value <= self._balance:
                self._balance -= value
                return self._balance

            print("(WARNING) - Not enough balance.")
            return self._balance
        except ValueError as e:
            print(f"(ERROR) - {e}")
            e.add_note("The value must be a number or you can't withdraw more than the balance.")
            return self._balance

    def __str__(self):
        return f"Agency: {self.agency}, Account Number: {self.account_number}, Balance: {self._balance}"
    