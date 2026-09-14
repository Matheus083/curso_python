# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.

# Ex.:
# with open('aula133_context_manager.txt', 'w') as file:
#     ...
class MyContextManager:

    def __init__(self, path_file, mode):
        self.path_file = path_file
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Opening file.')
        self._file = open(self.path_file, self.mode, encoding='utf-8')
        return self._file

    def __exit__(self, exc_type, exc, tb):
        print('Closing file.')
        self._file.close()

        raise ConnectionError("Is not possible to connect.")


instance = MyContextManager('aulas/aula133_context_manager.txt', 'w')

with instance as file:
    file.write('WITH - Gerenciador de Contexto com classes\n')
    file.write('O método __enter__ é chamado quando o bloco with é iniciado.\n')
    file.write('O método __exit__ é chamado quando o bloco with é finalizado.\n')

    print('WITH ', file)
