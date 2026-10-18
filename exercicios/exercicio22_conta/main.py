from accounts import CurrentAccount, SavingsAccount
from persons import Client
from bank import Bank


if __name__ == "__main__":
    # Cria o banco com sua agência
    bank = Bank("Bank of America", 12235)

    # Cria as contas
    current_account = CurrentAccount(12235, 12345)
    savings_account = SavingsAccount(12235, 54321)

    # Cria clientes vinculados às respectivas contas
    current_client = Client("John", 20, current_account)
    savings_client = Client("Mary", 25, savings_account)

    # Cadastra os clientes e suas contas no banco
    bank.add_client(current_client)
    bank.add_client(savings_client)

    # Realiza depósitos
    current_account.deposit(1000)
    savings_account.deposit(500)

    print("=== Saques autorizados ===")
    bank.withdraw(current_client, current_account, 200)
    bank.withdraw(savings_client, savings_account, 100)

    print(current_client)
    print(savings_client)

    print("\n=== Teste de autenticação ===")

    # Cliente cadastrado tentando sacar de conta alheia
    bank.withdraw(current_client, savings_account, 50)

    # Conta de agência diferente
    external_account = SavingsAccount(99999, 77777)
    bank.withdraw(current_client, external_account, 50)

    print("\n=== Estado do banco ===")
    print(bank)
