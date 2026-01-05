"""
Docstring for aulas.aula22_try_e_except
try -> tenta executar o código
except -> executa caso dê algum erro no try
"""

number_str = input('I wiil double the number you enter: ') 
try:
    print('STR', number_str)
    number_float = float(number_str)  # Converting string to float
    print('Float', number_float)
    print(f'The double of {number_str} is {number_float * 2}')
except:
    print('It is not a valid number')