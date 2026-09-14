# Context Manager com funcaos - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def myopen(path_file, mode):
    try:
        print('OPENING FILE')
        file = open(path_file, mode, encoding='utf-8')
        yield file

    except Exception as e:
        print('ERROR', e)
        
    finally:
        print('CLOSING FILE')
        file.close()

with myopen('aulas/aula134_context_manager.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    print('WITH',  file)
