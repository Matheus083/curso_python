''' 
split e join com list e str
split -> Dividir uma string # str
join -> une uma string # str
'''

phrase = 'The best way to learn is to teach'
words_list_old = phrase.split('e ') # por padrão o split separa pelos espaços


words_list = []
for i, phrase in enumerate(words_list_old):
    words_list.append(words_list_old[i].strip())

# print(words_list)
united_phrases = '-'.join(words_list)
print(united_phrases)

