"""Interpolação de strings em Python
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
name = "Maria"
price = 1000.95897643
variable = '%s, The price is R$%f' % (name, price)

print(variable)
print("The hexadecimal of %d is %05x " % (1500, 1500))
