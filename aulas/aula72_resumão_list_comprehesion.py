print(10 * '*', 'Basic - List Comprehension - Map', 10 * '*')
print()
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
multiply = [multiply(number, 2) for number in numbers] # map -> mapeando lista pra outra lista.

# new_numbers = []
# for number in numbers:
    # new_numbers.append(number)

# numbers[0] = 23
print(multiply)
print(numbers)

print()
print(10 * '*', 'Conditions - List Comprehension', 10 * '*')
print()


numbers_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers_two = [numbers for numbers in numbers_two if numbers > 4]
tests = [
        numbers_tests 
        if numbers_tests in [4, 5] else 620 
        for numbers_tests in numbers_two 
        if numbers_tests > 3
        ]
print(numbers_two)
print(new_numbers_two)
print(tests)
