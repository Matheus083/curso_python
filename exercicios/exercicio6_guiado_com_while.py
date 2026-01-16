"""
Iterando strings com while.
"""

counter = 0
name = 'Matheus Nunes'
total_letters = len(name)
new_name = '*'

while total_letters > counter:

    letter = name[counter]
    new_name += f'{letter}*'
    counter += 1

print(new_name)
