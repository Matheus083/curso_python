# Yield from.

def gen1():
    print('Starting gen1.')
    yield 1
    yield 2
    yield 3
    print('Ending gen1.')

def gen2(gen):
    print('Starting gen2.')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('Ending gen2.')

g = gen2(gen1)
for number in g:
    print(number)