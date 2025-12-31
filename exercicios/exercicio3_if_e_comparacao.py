# Exercício 3: Comparação de Números
Number_One = input("Typing the first number: ")
Number_Two = input("Typing the second number: ")
grater_Than_Or_Equal = float(Number_One) >= float(Number_Two)
less_Than_Or_Equal = float(Number_One) <= float(Number_Two)
not_Equal = float(Number_One) != float(Number_Two)
equal = float(Number_One) == float(Number_Two)

if grater_Than_Or_Equal:
    print(f"The number '{Number_One}' is greater than or equal to the number '{Number_Two}'.")
elif less_Than_Or_Equal:
    print(f"The number '{Number_Two}' is greater than or equal to the number '{Number_One}'.")
if not_Equal:
    print(f"The number '{Number_One}' is different from the number '{Number_Two}'.")
elif equal:
    print(f"The number '{Number_One}' is the same as the number '{Number_Two}'.")
