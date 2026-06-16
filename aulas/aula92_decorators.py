# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# Função decoradora.
def create_function(parameter):
    def inner_function(*args, **kwargs):
        print('I am decorating a function.')
        for arg in args:
            e_string(arg)
        result = parameter(*args, **kwargs)
        print(f"The result of the function is: {result}")
        print('I finished decorating the function.')
        return result
    return inner_function

@create_function
def reverse_string(string):
    print(f"{reverse_string.__name__} is being decorated.")
    return string[::-1]

def e_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError('There was a type error.')


reverse = reverse_string("Hello, World!")
print(reverse)
