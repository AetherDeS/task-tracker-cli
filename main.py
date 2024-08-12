# < -- TASK-TRACKER-CLI -- >

# Requirements
# Приложение должно запускаться из командной строки,
# принимать действия и вводимые пользователем данные в качестве аргументов и сохранять задачи в файле JSON.
# Пользователь должен иметь возможность:

# Добавление, обновление и удаление задач  -- add, edit, remove
# Отметить задачу как выполняющуюся или выполненную -- inp, done
# Список всех задач  -- default printing
# Перечислите все выполненные задачи -- dt
# Список всех задач, которые выполняются  -- inpt


# TODO:
# 1.      Создать аргументы: 
# 1.1.    Добавления, обновления и удаления задачи
# 2.      Создать функции для аргументов


# Работать будет необходимо с библиотекой 'arpgarse'
import argparse
import os.path

file = 'todo_list.json'

# Читает список дел, если его нет --> создаёт.
def todo_list_read():
    if os.path.exists(file) == False:
        todo_list_create()

    with open(file, 'r') as f:
        data = f.read()
    if len(data) <= 1:
        data = '< -- Todo list is clear -- >'
    return data

#
def todo_list_create():
    with open(file, 'w') as f:
        f.write('')

def todo_list_task_add(task):
    with open(file, 'w') as f:
        f.write(task)

def todo_list_task_remove():
    pass

def todo_list_task_edit():
    pass

def done_tasks_show():
    pass

def in_process_tasks_show():
    pass

def task_count_calculate():
    with open('todo_list.json', 'r') as f:
        data = f.readlines()
        return data


def main():
# Создаём парсер аргументов
    parser = argparse.ArgumentParser(
        prog='TASK-TRACKER-CLI',
        description='Эта программа позволяет вам формировать свой список дел. Все ваши дела хранятся в JSON-файле.',
        epilog='Если вы хотите отобразить список дел, просто запустите программу')

# Перед тем как создавать аргументы стоит помнить что '-h' и '--help' созданы уже за вас по умолчанию
    #parser.add_argument('--todo_list', type=str, help='Отображает список дел')
    parser.add_argument('-action', type=str, choices=['add', 'edit', 'remove'], help='Обязательный параметр, принимает действие, которое необходимо осуществить с JSON файлом.')
    parser.add_argument('task', metavar='sentence', type=str, nargs='+', help='Task')
    parser.add_argument('-status', type=str, choices=['inp', 'done'], help='Позволяет отмечать задачи как выполняющиеся, или завершенные')
    # parser.add_argument()

    args = parser.parse_args()

    if args.action == 'inp':
        in_process_tasks_show()
    elif args.action == 'add':
        todo_list_task_add(args.task)
    else:
       print(todo_list_read())

print(task_count_calculate())

if __name__ == '__main__':
    main()
