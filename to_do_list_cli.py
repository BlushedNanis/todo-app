import functions
from time import strftime

now = strftime("%b %d, %Y - %H:%M:%S")
print("It is: ", now)

while True:
    user_input = input("Type add, show, edit, complete or exit: ")
    user_input = user_input.strip()
    
    if user_input.startswith("add"):
        todo = user_input[4:].capitalize() + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
            
    elif user_input.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
            
    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo.capitalize() + '\n'
            functions.write_todos(todos)
        except ValueError as error:
            print(error, 'The value of the todo must be an integer')
            continue
        except IndexError as error:
            print(error,"There is no item with that number")
            continue
            
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_complete = todos[index].strip('\n')
            print(f"The todo '{todo_to_complete}' has been completed")
            todos.pop(index)
            functions.write_todos(todos)
        except ValueError as error:
            print(error, 'The value of the todo must be an integer')
            continue
        except IndexError as error:
            print(error,"There is no item with that number")
            continue
                
    elif user_input.startswith("exit"):
        break
    
    else:
        print("Unknown command")

print("Goodbye!")