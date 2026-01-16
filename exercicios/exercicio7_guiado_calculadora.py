"""Calculadora com while"""

turn_on = True

while turn_on:

    try:

        operator = str(input('Typing the operation you want to perform (+, -, *, /): '))

        while operator not in ('+', '-', '*', '/'):
            operator = str(input('Invalid operator. Please type one of the following (+, -, *, /): '))

        number_one = float(input('Type the first number: '))
        number_two = float(input('Type the second number: '))

        while operator in ('+', '-', '*', '/'):
            
            
            if operator == '+':
                result = number_one + number_two

            elif operator == '-':
                result = number_one - number_two

            elif operator == '*':
                result = number_one * number_two

            elif operator == '/':
                if number_two != 0:
                    result = number_one / number_two

                else:
                    result = 'Error: Division by zero is not allowed.'
            
            print(f'The result of {number_one} {operator} {number_two} is: {result}')
            
            operator = str(input('Typing the operation you want to perform (+, -, *, /) or any other key to exit: '))

            if operator in ('+', '-', '*', '/'):
                number_one = float(input('Type the first number: '))
                number_two = float(input('Type the second number: '))

            elif operator == 'exit':
                print('Exiting the calculator. Goodbye!')
                turn_on = False
                
            else:
                print('Invalid operator.')
    except:
        print('Error: Invalid input. Please enter numeric values for numbers and valid operators.')
