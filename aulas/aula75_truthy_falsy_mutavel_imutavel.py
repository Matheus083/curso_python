# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis.
# Mutáveis [] {} set().
# Imutáveis () "" 0 0.0 None False range().

list1 = []
dict1 = {}
set1 = set()
tuple1 = ()
string1 = ''
int1 = 0
float1 = 0.0
bool1 = False
nothing1 = None
range1 = range(0)

def falsy(value):
    return 'falsy' if not value else 'truthy'

print(f'TEST', falsy('TEST'))
print(f'{list1=}', falsy(list1))
print(f'{dict1=}', falsy(dict1))
print(f'{set1=}', falsy(set1))
print(f'{tuple1=}', falsy(tuple1))
print(f'{string1=}', falsy(string1))
print(f'{int1=}', falsy(int1))
print(f'{float1=}', falsy(float1))
print(f'{bool1=}', falsy(bool1))
print(f'{nothing1=}', falsy(nothing1))
print(f'{range1=}', falsy(range1))

