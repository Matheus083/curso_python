# Empacotamento e Desempacotamento de dicionários.
a, b = 1, 2
a, b = b, a

# print(a, b)

person = {
    'name': 'Lucas',
    'lastname': 'Vitor',
}

# (a1, a2), b  = person.items()
# print(a1, a2)
# print(b)


# for key, value in person.items():
#     print(value)
'''
args e kwargs 
args (já vimos)
kwargs - keywords arguments (argumentos nomeados)
'''

data = {
    'age': 19,
    'height': 1.84
}

person_complete = {**person, **data}

# print(person_complete)

def named_args(*args, **kwargs):
    print('NOT NOMED:', args)
    for key, value in kwargs.items():
        print(key, value)

named_args('João',name='Matheus', qlq=123)
print()
named_args(**person_complete)
