name = input("Typing your name: ")
age = input("Typing your age: ")

if len(name) and len(age) >= 1:
    print(f"Your name is {name}")
    print(f"You are {age} years old")
    print(f"Your inverse name is {name[::-1]}")
    if " " in name:
        print("Your name has spaces")
    else:
        print("Your name does not have spaces")
    print(f"Your name has {len(name)} letters")
    print(f"The first letter of your name is {name[0]}")
    print(f"The last letter of your name is {name[-1]}")
else:
    print("You did not type correctly the name or age.")
    