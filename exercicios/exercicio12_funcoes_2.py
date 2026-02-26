# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def create_multiplier(number):
    def double():
        return number * 2
    def triple():
        return number * 3
    def quadruple():
        return number * 4
    return double, triple, quadruple

number = 5
double, triple, quadruple = create_multiplier(number)
print(f"The Double {number} is: {double()}")
print(f"The Triple {number} is: {triple()}")    
print(f"The Quadruple {number} is: {quadruple()}")
