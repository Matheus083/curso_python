# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recursive(started=0, finished=10):
    # Caso base.
    if started >= finished:
        return print(finished)

    print(started)
    
    # Caso recursivo.
    # Contar até chegar ao final.
    started += 1
    return recursive(started, finished)


recursive()

