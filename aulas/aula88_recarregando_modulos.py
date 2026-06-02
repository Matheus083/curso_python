import aula89_teste
import importlib

for t in range(3):
    print(f'Iterator: {t}')
    importlib.reload(aula89_teste)

print('Finished modules.')
