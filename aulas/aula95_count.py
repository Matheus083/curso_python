# count é um contador infinito sem fim.
from itertools import count

c1 = count()
r1 = range(10)

print('c1:', hasattr(c1, '__iter__'))
print('c1:', hasattr(c1, '__next__'))
print('r1:', hasattr(r1, '__iter__'))
print('r1:', hasattr(r1, '__next__'))

for i in c1:
    print(i)

    