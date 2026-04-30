# Introdução às Generators Functions em Python.
# generator = (n for n in range(100000))

# def generator(n=0):
#     yield 1 # Pausar
#     print('Code after yield.')
#     yield 2 # Pausar novamente, permitindo que o próximo valor seja obtido.
#     print('Code after yield 2.')
#     return 'Finished' # Finalizar a função generator, retornando o valor 'Finished'.

def generator2(n=0, maximum=10):
    while True:
        yield n

        n += 1

        if n > maximum:
            return  # Finaliza a função generator2 quando n atingir ou ultrapassar o valor máximo definido.

        

# gen = generator(n=0)
# print(next(gen))  # Imprime o valor retornado pela função generator, que é 1.
# print(next(gen))  # Tenta obter o próximo valor da função generator, mas como ela já foi finalizada, gera uma exceção StopIteration.

gen2 = generator2(n=0)
for n in gen2:
    print(n)  # Imprime os valores gerados pela função generator2, que são infinitos, pois a função é um loop infinito.
