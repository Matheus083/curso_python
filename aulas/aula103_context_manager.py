import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

path = 'aulas/aula103_context_manager.txt'
with open(path, 'w+', encoding='utf-8') as file:
    # print(type(file))

    file.write('Line 1\n')
    file.write('Line 2\n')
    file.writelines(('Line 3\n', 'Line 4\n'))
    file.seek(0, 0)

    print('##### FIRST READING #####')
    print(file.read())
    
    file.seek(0, 0)
    
    print(file.readline(), end='')
    print(file.readline().strip())
    print(file.readline().strip())
    print('##### READLINES #####')
    
    file.seek(0, 0)
    
    for line in file.readlines():
        print(line.strip())

print('#' * 10)

with open(path, 'r') as file:
    print(file.read())

# file = open(path, 'w')

# file.close()

# os.unlink(path)
