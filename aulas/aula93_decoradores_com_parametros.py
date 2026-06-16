# Decoradores com parâmetros.
def factory_decorators(a=None, b=None, c=None):
    def factory_functions(func):
        print('Decorator 1')

        def nested(*args, **kwargs):
            print(f'Parameters: {a}, {b}, {c}')
            print('Nested')
            result = func(*args, **kwargs)
            return result
        return nested 
    return factory_functions


@factory_decorators(1, 2, 3)
def soma(a, b):
    return a + b

decorator = factory_decorators()
multiply  = decorator(lambda x, y: x * y)

ten_plus_five = soma(10, 5)
equal_to_ten = multiply(2, 5)
print(ten_plus_five)
print(equal_to_ten)
