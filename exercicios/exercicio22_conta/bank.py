class Bank:
    def __init__(self, name_bank, agency):
        self._name_bank = name_bank
        self._agency = agency
        self._clients = []
        self._accounts = []

    @property
    def name_bank(self):
        return self._name_bank

    @property
    def agency(self):
        return self._agency

    @property
    def clients(self):
        return self._clients

    @property
    def accounts(self):
        return self._accounts

    def add_client(self, client):
        if client not in self._clients:
            self._clients.append(client)

        if client.account not in self._accounts:
            self._accounts.append(client.account)

    

    def verify_agency(self, account):
        return account.agency == self._agency

    def verify_client(self, client):
        return client in self._clients

    def verify_account(self, account):
        return account in self._accounts

    def authenticate(self, client, account):
        return (
            self.verify_agency(account) 
            and self.verify_client(client) 
            and self.verify_account(account) 
            and client.account is account
            )

    def withdraw(self, client, account, value):
        if not self.authenticate(client, account):
            print('(ERROR) - Bank authentication failed.')
            return account.balance

        return account.withdraw(value)

    
    def __str__(self):
        clients = "\n".join(str(client) for client in self._clients)
        accounts = "\n".join(str(account) for account in self._accounts)
        return f"Bank: {self._name_bank}\nAgency: {self._agency}\nClients:\n{clients}\nAccounts:\n{accounts}"
