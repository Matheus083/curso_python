# Generator expression, Iterables and Iterators in Python.
import sys

iterable = ['I', 'Have', '__iter__']
iterator = iterable.__iter__() # Tem __iter__() e __next__().

# print(next(iterator)) 
# print(next(iterator))
# print(next(iterator))

list1 = [n for n in range(10000)]
generator = (n for n in range(100000))
print(list1)
print(generator)
print(sys.getsizeof(list1))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))