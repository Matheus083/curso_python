# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def divide(n, d):
    try:
        if d == 0:
            raise ZeroDivisionError('You can\'t divide by zero.')
        return n / d
    except ZeroDivisionError as e:
        return n
    
    