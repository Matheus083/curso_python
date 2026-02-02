# Imprecisão de ponto flutuante
# Double-precision floating-point format IEEE 754
# https://en.wikipedia.org/wiki/Double-precision_floating-point_format
# https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
import decimal

number_one = decimal.Decimal('0.1')
number_two = decimal.Decimal('0.2')
total = number_one + number_two

print(total)
print(f'{total:.2f}')
print(round(total, 2))
