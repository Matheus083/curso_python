""" while/else """

string = "Python"
i = 0 

while i < len(string):

    letter = string[i]

    # break
    print(letter)

    i += 1

else:
    print('The else block was executed.')

print('Out of the loop.')