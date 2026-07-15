# Problema dos parâmetros mutáveis
# - Parâmetros mutáveis podem ser alterados dentro da função
# - Parâmetros mutáveis podem ser alterados fora da função

def add_customers(name, list1=None):
    if list1 is None:
        list1 = []
    list1.append(name)
    return list1

customer_one = add_customers('Matheus')
add_customers('Beatriz', customer_one)
print(customer_one)
