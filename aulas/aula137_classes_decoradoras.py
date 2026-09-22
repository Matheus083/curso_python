# Classes decoradoras - Decorators

class Decorator:
    def __init__(self, multiplier):
        # self.func = func
        self._multiplier = multiplier
        

    def __call__(self, func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiplier
        return inner



@Decorator(10)
def sum1(x, y):
    return x + y

two_plus_three = sum1(2, 3)
print(two_plus_three)
