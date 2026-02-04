import sys
import random

# Gerando um CPF aleatório para teste.
# for i in range(9):
#     print(random.randint(0, 9), end='')
# print()

primary_cpf = '746.824.890-70'
# Pegando o CPF do usuário.
input_cpf = str(input("Typing the CPF: ")).replace('.', '').replace('-', '').replace(' ', '')
sequency_enter = input_cpf == input_cpf[0] * len(input_cpf)

if sequency_enter == True:
    print('The CPF is invalid.')
    sys.exit()

# Multiplicando cada dígito do CPF por um peso específico e somando os resultados.
value_multiplied = 0

wheight = 10
for i in range(len(input_cpf)):
    value_multiplied += int(input_cpf[i]) * wheight
    wheight -= 1

# multiplicando o resultado por 10 e dividindo por 11 para obter o primeiro dígito verificador.
value_multiplied = value_multiplied * 10
first_digit = value_multiplied % 11
first_digit = 0 if first_digit >= 10 else first_digit

print('The first digit is: ', first_digit)

# Repetindo o processo para obter o segundo dígito verificador.
value_multiplied = 0
wheight = 11
input_cpf += str(first_digit)

for i in range(len(input_cpf)):
    value_multiplied += int(input_cpf[i]) * wheight
    wheight -= 1
    
# multiplicando o resultado por 10 e dividindo por 11 para obter o segundo dígito verificador.
value_multiplied = value_multiplied * 10
second_digit = value_multiplied % 11
second_digit = 0 if second_digit >= 10 else second_digit

print('The second digit is: ', second_digit)

# Mostrando o CPF completo com os dígitos verificadores.
cpf = input_cpf + str(second_digit)
cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
print('The complete CPF is: ', cpf)

# Verificando se o CPF é válido.
if cpf != primary_cpf:
    print('The CPF is invalid.')

else:
    print('The CPF is valid.')
