'''
Docstring for aulas.aula13_if_elif_else
if / elif / else statements in Python
se / se não se/ senão em Python
'''
entry = input('Você quer entrar na festa? (s/n) ')

if entry == 's':
    print('Você pode entrar na festa!')
elif entry == 'n':
    print('Você não pode entrar na festa!')
else:
    print('Resposta inválida. Por favor, responda com "s" ou "n".')
