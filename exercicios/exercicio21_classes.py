# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Manufacturer:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, name, manufacturer=None, engine=None):
        self.__name = name
        self.__manufacturer = manufacturer
        self.__engine = engine

        @property
        def manufacturer(self):
            return self.__manufacturer
        
        @manufacturer.setter
        def manufacturer(self, manufacturer):
            self.__manufacturer = manufacturer

        @property
        def engine(self):
            return self.__engine
        
        @engine.setter
        def engine(self, engine):
            self.__engine = engine

        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, name):
            self.__name = name
        
    def info(self):
        m_name = self.__manufacturer.name if self.__manufacturer else "Without Manufacturer"
        e_name = self.__engine.name if self.__engine else "Without Engine"
        
        print(f'Car: {self.__name} | Engine: {e_name} | Manufacturer: {m_name}')

class Engine:
    def __init__(self, name):
        self.name = name

ford = Manufacturer('Ford')
engine = Engine('Lt-400c')
car = Car('Ka-2016', ford, engine)
car.info()


chevrolet = Manufacturer('Chevrolet')
engine_chevrolet = Engine('SV-1000R')
car_chevrolet = Car('Cruze LM', chevrolet, engine_chevrolet)
car_chevrolet.info()
