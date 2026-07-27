# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MyString(str):

    def __init__(self, commit):
        self.commit = commit

    def upper(self):
        print('CALL UPPER!')
        return super().upper()

    
class Test(MyString):
    attr = 'Test'

    def __init__(self, commit, other_commit):
        super().__init__(commit)
        self.other_commit = other_commit    

string = MyString('Matheus')
test = Test('commit1', 'TESTE')
print(test.lower())
print(string.upper())

