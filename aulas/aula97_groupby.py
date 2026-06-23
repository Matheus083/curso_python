# groupby - agrupando valores (itertools)
from itertools import groupby

students = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

grouped_students = sorted(students, key=lambda a: a['nota'])

# for s in grouped_students:
#     print(s)


groups_2 = groupby(grouped_students, key=lambda a: a['nota']) 
# print(list(groups))

for key_2, group_2 in groups_2:
    print(key_2)
    for student in group_2:
        print(student)
