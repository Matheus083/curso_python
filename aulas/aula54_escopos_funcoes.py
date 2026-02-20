''' 
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
'''
x = 1
print(x)

def scope():
    global x
    def otherScope(a, b):
        global x
        y = a
        z = b
        print(y + z)
    x = 11
    print(x)
    otherScope(2, 3)

scope() # 10
print(x) # 1  
  