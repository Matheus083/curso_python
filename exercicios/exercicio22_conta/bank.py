class Bank:
    def __init__(self, name_bank, client, account):
        self._name_bank = name_bank
        self._client = client
        self._account = account

    @property
    def name_bank(self):
        return self._name_bank

    @name_bank.setter
    def name_bank(self, value):
        self._name_bank = value

    def __str__(self):
        return f"Bank: {self._name_bank}\nClient: {self._client}\nAccount: {self._account}"
