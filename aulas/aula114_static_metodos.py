# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.
class Class:
    @staticmethod
    def function_class(*args, **kwargs):
        print('Hello', args, kwargs)

c1 = Class()
c1.function_class(1,2,3)
Class.function_class(named=1)
