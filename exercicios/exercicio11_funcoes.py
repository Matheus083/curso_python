# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiply(*args):
    total = 1
    for num in args:
        if num == 0:
            return 0
        total *= num
    return total

result = multiply(2, 3, 4)
print(result)  # Output: 24

result = multiply(2, 0, 4)
print(result)  # Output: 0

# Par ou ímpar
def is_even_or_odd(*num):
    for n in num:
        if n % 2 == 0:
            print(f"{n} é par.")
        else:
            print(f"{n} é ímpar.")

is_even_or_odd(1, 2, 3, 4, 5)
