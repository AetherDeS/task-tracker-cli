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
from argparse import ArgumentParser

file = 'todo_list.json'


def todo_list_add(letter):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{letter}\n')

def todo_list_show():
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            count = len(data)
            print(f'Tasks in your list: {count}')
            for i, t in enumerate(data):
                print(f'{i+1}. {t}')
    except FileNotFoundError:
        with open(file, 'w') as f:
            f.write('')
        print('File load success. Repeat command.')
        

def main():
    parser = ArgumentParser(prog='TASK-TRACKER', description='This program allow you track your tasks', epilog='--help')
    

    parser.add_argument('-a', '--action', action='store')
#     parser.add_argument('task', nargs='+', help='Your sentence for action')
    args = parser.parse_args()

    if args.action == 'show':
         todo_list_show()
    elif args.action == 'add':
#        try:
        todo_list_add(input())
#        except TypeError:
#        print(' < -- Error! -- > \nYou need write task. \nExample: python main.py add \" some task \"')

#    if args.action == '1':
#        print('2')
#    if args.action == '2':
#        print('3')


if __name__ == '__main__':
    main()

# second commit, one more commit

