sum_lambda = lambda x, y: print(x + y) 
sum_lambda(7,5)

def exec(function, *args):
    return function(*args)

multiplicator =  exec(lambda f: lambda n: n*f , 5)

print(multiplicator(6))
print(exec(lambda *args: sum(args), 99,2,64,5459,0,6,3,8,43,87645,5))

