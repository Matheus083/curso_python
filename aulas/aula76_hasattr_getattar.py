# dir, hasattr e getattr em Python.

string = 'Matheus'
methood = 'upper'

# dir() -> Mostra os atributos e métodos de um objeto.
print(dir(string))
# hasattr() -> Verifica se um objeto tem um atributo ou método.
print(hasattr(string, methood))
# getattr() -> Retorna o valor de um atributo ou método de um objeto.
print(getattr(string, methood)())

if hasattr(string, methood):
    print('Exist a method.')
    print(getattr(string, methood)())
else:
    print('Not exist a method.', methood)
