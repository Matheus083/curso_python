# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

"""
AULA 01 - DATETIME

# date_ = datetime(2026, 10, 28)
# date_str_data = '28-10-2026 22:02:37'
# data_str_format = '%d-%m-%Y %H:%M:%S'
# date_2 = datetime.strptime(date_str_data, data_str_format)

# print(date_2)
"""
date = datetime.now(timezone('America/Recife'))
print(date)
print(date.timestamp())
