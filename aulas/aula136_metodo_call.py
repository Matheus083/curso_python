# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe():
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print(f'Calling {self.phone}')

call1 = CallMe('1234-5678')
call2 = CallMe('8765-4321')

call1()
call2()
