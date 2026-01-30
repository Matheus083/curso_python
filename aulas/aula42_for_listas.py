'''
for in listas
'''

'''
array = ['Pedro', 'Hiago', 'Vitor', 'Eduardo']
i = 0

for word in array:
    print(i, word)
    i += 1
'''

# enumarate - enumera interáveis (índices)

array = ['Maria', 'Helena', 'Luiz']
array.append('Matheus')

# array_enumerate = enumerate(array)

# print(array_enumerate)

# print(next(array_enumerate))
# print(next(array_enumerate))

# for i in array_enumerate:
#     print(i) 

# array_list = list(enumerate(array))

# print(array_list)

for index, name in enumerate(array):
    print(index, name)