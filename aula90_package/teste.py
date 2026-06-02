import sys
import os

# Adiciona o diretório atual ao path
# sys.path.append(os.path.abspath(os.curdir))
print(__name__)

from aula90_teste import sum_plus
print(sum_plus(5, 10))
