person = {
    'name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'height': 1.75,
    'adresses': [
        {
            'street': 'Main Street',
            'number': 123,
            'city': 'New York',
            'state': 'NY',
            'country': 'USA'
        },
        {
            'street': 'Second Street',
            'number': 456,
            'city': 'Los Angeles',
            'state': 'CA',
            'country': 'USA'
        }
    ]
}

# person['mother'] = 'Jane'
# print(person)

del person['adresses'][1]
print(person['adresses'])
