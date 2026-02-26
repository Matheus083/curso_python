import copy

person= {
    'name': 'John',
    'last_name': 'Doe',
    'age': 30,
}

# person_test1 = person # assignment
person_test = person.copy() # shallow copy
# person_test1['name'] = 'Jane'
# print(person) # {'name': 'John', 'last_name': 'Doe', 'age': 30}
# print(person_test) # {'name': 'Jane', 'last_name': 'Doe', 'age':  +30}
# print(person_test1) # {'name': 'Jane', 'last_name': 'Doe', 'age': 30}
person_test2 = copy.deepcopy(person) # shallow copy

