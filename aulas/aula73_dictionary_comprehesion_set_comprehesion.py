# Dictionary Comprehension e Set Comprehension.

product = {
    'name': 'Blue Pencil',
    'price': 10,
    'Category': 'Office',
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key != 'price'
}

s1 = {i * 4 for i in range(11) if i % 2 == 0}
print(s1)

