# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Line 1'[1000])
    c = a / b
    print('Line 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Name b is not defined')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Name:', error.__class__.__name__)
except Exception:
    print('Error ocurred.')

print('CONTINUE.')
