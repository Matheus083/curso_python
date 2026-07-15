# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# array_tasks = []
# while True:
#     count_array_tasks = len(array_tasks)
#     try:
#         user = str(input('Choose your option: (ADD), (LIST), (UNDO), (REDO) and (CLEAR): '))
#     except Exception as e:
#         print("Choose only one of the options above.\n")

#     if user.lower() == 'add':
#         task = str(input('Typing your task: '))
#         print()
#         try:
#             if isinstance(task, str):
#                 array_tasks.append(task)
#                 continue
#             if task == '' or task.isspace():
#                 print('You typing null.') 
#                 continue
#         except Exception as e:
#             print('Typing only Strings.')
#             continue

#     if user.lower() == 'list':
#         for i, tasks in enumerate(array_tasks):
#             print(i, tasks)
#         continue

#     if user.lower() == 'undo':
#         array_undo = []
#         if len(array_tasks) == 0:
#             print("List is null. You can't use this option. ")
#             continue
#         array_undo.append(array_tasks.pop())
#         continue

#     if user.lower() == 'redo':   
#         if not 'array_undo' in locals():
#             print('You need to add something first.')
#             continue
#         elif len(array_undo) == 0: 
#             print("Ops! There is nothing left to redo. ")
#             continue
        
#         array_tasks.append(array_undo[-1])
#         array_undo.pop(0)
#         continue

#     if user.lower() == 'clear':
#         array_tasks.clear()
#         continue

#     else:
#         print('Please, typing one of the valids options.')

# Codigo feito por ia completo.
import json

def list_task(task: list[str]) -> None:
    
    if not task:
        print("You need to add something first.")
        return

    print("\n=== YOUR TASKS ===")
    for i, task in enumerate(task, start=1):
        print(f"{i}. {task}")

def add_task(task: str, tasks: list[str], history_redo: list[str]) -> None:
    task_clear = task.strip()

    if not task_clear:
        print("\n[Error] Is not possible to add an empty task.")
        return
    
    tasks.append(task_clear)
    history_redo.clear()
    print(f"\n[+] Task '{task_clear}' added with success.")

def undo(tasks: list[str], history_redo: list[str]) -> None:
    if not tasks:
        print("\n[!] There is nothing to undo.")
        return
    
    last_task = tasks.pop()
    history_redo.append(last_task)
    print(f"\n[-] Undo '{last_task} removed with success.")

def redo(tasks: list[str], history_redo: list[str]) -> None:
    if not history_redo:
        print("\n[!] There is nothing to redo.")
        return
    
    recupered_task = history_redo.pop()
    tasks.append(recupered_task)
    print(f"\n[+] Redo '{recupered_task}' added with success.")

def clear(tasks: list[str], history_redo: list[str]) -> None:
    tasks.clear()
    history_redo.clear()
    print("\n[!] All tasks removed with success.")

def pull_datas():
    try:
        with open('exercicios/exercicio19.json', 'r', encoding='utf8') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save_datas(tasks):
    with open('exercicios/exercicio19.json', 'w', encoding='utf8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def main():
    list_tasks = pull_datas()
    history_redo = []

    options = {
        'add': lambda: add_task(input("Type your task: "), list_tasks, history_redo),
        'list': lambda: list_task(list_tasks),
        'undo': lambda: undo(list_tasks, history_redo),
        'redo': lambda: redo(list_tasks, history_redo),
        'clear': lambda: clear(list_tasks, history_redo),
    }

    while True:
        print("\nOptions: [ADD] [LIST] [UNDO] [REDO] [CLEAR] or [EXIT] to finish.")
        choose = input("Choose one option: ").strip().lower()

        if choose == 'exit':
            print("\nLeave the program. See you later.")
            break

        action = options.get(choose)

        if action:
            action()
            save_datas(list_tasks)
        else:
            print("\n[Error] Invalid option. Try again.")

if __name__ == "__main__":
    main()
