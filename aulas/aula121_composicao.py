# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Customer:
    def __init__(self, name):
        self.name = name
        self.address = []

    def insert_endereco(self, street, number):
        self.address.append(Address(street, number))

class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

customer1 = Customer('Matheus')
customer1.insert_endereco('Rua adriano tozzi carvalho', 245)
customer1.insert_endereco('AV.Brasil', 1310)

print(customer1.address[0].street)
print(customer1.address[0].number)
