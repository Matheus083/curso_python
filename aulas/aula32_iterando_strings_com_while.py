phrase = 'The python is a programming language. ' \
    'Created by Guido van Rossum. '\
    'Python is free to use, even for commercial applications.'

# print(phrase.lower().count('python'))  # Case sensitive
# print(phrase.count('a'))

i = 0

number_of_letters_that_appeared_most_times = 0
lettes_times = ''

while i < len(phrase):

    current_letter = phrase[i]
    amount_letters = phrase.count(current_letter)

    if current_letter == ' ':
        i += 1
        continue
    if  amount_letters > number_of_letters_that_appeared_most_times:
        number_of_letters_that_appeared_most_times = amount_letters
        lettes_times = current_letter



    i += 1

print(f'The letter that appeared the most times was "{lettes_times}" and appeared {number_of_letters_that_appeared_most_times} times.')
