# Funcoes decoradoras e decoradores de classes.

def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

def my_planet(method):
    def inside(self, *args, **kwargs):
        result = method(self, *args, **kwargs) 

        if 'Terra' in result:
            result = f"{result} - This is our planet!"
            
        return result
    return inside

@add_repr
class Team:
    def __init__(self, name):
        self.name = name

@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def speak_name(self):
        return f"The name of the planet is {self.name}"

brasil = Team("Brasil")
portugal = Team("Portugal")
terra = Planet("Terra")
venus = Planet("Venus")

print(brasil)
print(portugal)
print()
print(terra)
print(venus)
print()
print(terra.speak_name())
print(venus.speak_name())
