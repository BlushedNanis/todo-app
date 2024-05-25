import functions
import PySimpleGUI as sg
from time import strftime
from os import path


# Create text file if doesn't exists
if not path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('DarkGrey11')

# Create GUI instances
enter_todo_label = sg.Text("Enter a to-do:")
clock_label = sg.Text('')
input_box = sg.InputText(tooltip='Enter a to-do:', key='todo')
add_button = sg.Button('Add')
todos_box = sg.Listbox(functions.get_todos(), key = 'selected_todo',
                       size = (30,15), enable_events = True)
complete_button = sg.Button('Complete')
edit_button = sg.Button('Edit')
exit_button = sg.Button('Exit')

# Set GUI window
window = sg.Window('To-do App',
                   font=('Verdana', 10),
                   layout=[[clock_label],
                           [enter_todo_label],
                           [input_box, add_button],
                           [todos_box, complete_button, edit_button],
                           [exit_button]])

while True:
    # Main loop
    event, values = window.read(timeout=500)
    
    match event:
        # Catch user interactions
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'].capitalize() + '\n')
            functions.write_todos(todos)
            todos_box.update(todos)
            input_box.update('')
            
        case 'selected_todo':
            input_box.update(values['selected_todo'][0].strip('\n'))
            
        case 'Complete':
            try:
                todos = functions.get_todos()
                todos.remove(values['selected_todo'][0])
                functions.write_todos(todos)
                todos_box.update(todos)
                input_box.update('')
            except IndexError:
                sg.popup("First select the todo from the list,"
                        "\nthen press the COMPLETE button",
                        font=('Verdana', 10))
                continue
            
        case 'Edit':
            try:
                todos = functions.get_todos()
                todo_index = int(todos.index(values['selected_todo'][0]))
                todos[todo_index] = values['todo'].capitalize() + '\n'
                functions.write_todos(todos)
                todos_box.update(todos)
            except IndexError:
                sg.popup("First select the todo from the list,"
                        "then type a new todo\nand finally "
                        "press the EDIT button",
                        font=('Verdana', 10))
                continue
            
        case 'Exit':
            break
        
        case sg.WIN_CLOSED:
            break
        
    # Update time    
    clock_label.update(strftime("%b %d, %Y - %H:%M:%S"))
    
window.close()