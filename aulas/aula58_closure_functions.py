'''
Closure e funções  que retornam outras funções.
'''

def create_greeting(greeting, name):
    def greeting_message():
        return f'{greeting}, {name}!'
    
    return greeting_message

s1 = create_greeting('Olá', 'João')
s2 = create_greeting('Oi', 'Maria')
print(s1())
print(s2())
 