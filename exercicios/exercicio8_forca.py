key_word = 'Beatriz'
checked = ''
index = 0
counter = 0

print(15*'-',"You're welcome the Game!!!",15*'-')

while counter <= 6:

    word_typing = str(input('Typing the letter: '))

    if word_typing in checked:
        print('')
        if word_typing.lower() in key_word.lower():

            print('Yes!', word_typing)

            counter += 1
            checked += word_typing

    index += 1
