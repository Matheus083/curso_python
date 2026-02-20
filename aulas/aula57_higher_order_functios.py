"""
Higher Order Functions
Funções de primeira classe
"""

def greeting(msg):
    return msg

# greetings = greeting
# print(greetings('Hello World!'))

def run(func, *args):
    return func(*args)

v = run(greeting, 'Hello World!')
print(v)
