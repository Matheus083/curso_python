# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.preco for p in self._products])
    
    def insert_products(self, *products):
        for product in products:
            self._products.append(product)
    
    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.preco)
        print()

class Product:
    def __init__(self, name, preco):
        self.name = name
        self.preco = preco

cart = Cart()
p1, p2 = Product('Pen', 1.2), Product('Shirt', 20)
cart.insert_products(p1, p2)
cart.list_products()
print(cart.total())
