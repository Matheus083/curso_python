# Exemplo de uso dos sets
letters = set()

while True:
    letter = input('Type a letter: ')
    letters.add(letter)

    if letter == 'exit':
        break

    
    print(f'You have typed the following letters: {letters}')
