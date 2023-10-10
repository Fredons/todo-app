from functions import *
import time

now = time.strftime('%d - %b - %Y   %H:%M:%S')
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
        print(f"'{todo}' has been to your todo list")

    elif user_action.startswith('show'):
        todos = get_todos()
        # let's remove the extra lines from the todos using list comprehension'
        # new_todos = [task.strip('\n') for task in todos]

        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')  # this is to remove the extra
            # lines gotten from having '\n' in the todos lists

            print(f"{index + 1}.{item}")
    elif user_action.startswith('edit'):
        try:
            edited = int(user_action[5:])
            edited = edited - 1

            todos = get_todos()

            new_entry = input("Now enter your new todo item: ")
            todos[edited] = new_entry + '\n'

            write_todos(todos)
            print(new_entry, "has been updated to your todo list")
        except (ValueError, IndexError):
            print("Your command is invalid")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_task = int(user_action[9:])
            todos = get_todos()
            completed_task = todos.pop(completed_task - 1).strip('\n')
            write_todos(todos)

            print(f"{completed_task} task completed and removed from todo list. type 'show to see list'")
        except (IndexError, ValueError):
            print("Your command is invalid")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Sorry, the command you entered is not valid.")
print('Bye')
