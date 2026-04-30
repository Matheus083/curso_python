# Try, except, else e finally.
try:
    a = 18
    b = 0
    print('Line 1.' [1000])
    c = a / b
    print('Line 2.')
except ZeroDivisionError:
    print('Divided by zero.')
except NameError:
    print('Name b is not defined. It is a name error.')
except(TypeError, IndexError):
    print('Type error or index error.')
except Exception:
    print('An error occurred.')

print('Continues...')