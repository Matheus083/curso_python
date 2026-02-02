"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os 

active_or_not = True
list_shopping = []

try:
    while active_or_not == True:
        option_user = str(input('Select an option: \n (i)nsert,  (d)elete,  (l)ist:  ')).lower()

        if option_user == 'i':
            os.system('clear')
            item_insert = str(input('Type the item to insert: '))
            list_shopping.append(item_insert)
            print(f'Item "{item_insert}" inserted successfully!')

        elif option_user == 'd':
            item_delete = str(input('type the number of the item to delete: '))
            if item_delete.isdigit():
                item_delete = int(item_delete) 
                if 0 < item_delete <= len(list_shopping):
                    removed_item = list_shopping.pop(item_delete - 1)
                    print(f'Item "{removed_item}" deleted successfully!')
                else:
                    print('Error: Invalid index. Please try again.')
        else:
            print('Current shopping list:')
            for index, item in enumerate(list_shopping, start=1):
                print(f'{index}. {item}')
except: 
    print('An unexpected error occurred. Please try again.')
