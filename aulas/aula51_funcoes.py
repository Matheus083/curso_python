"""
Introdução às funções (def) em Python.
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None, caso não haja um return explícito.
"""

def Python():
    print('Python')

Python()

def sum(a=0, b=0):
    return a + b

print(sum(2, 3))
print(sum()) 
