import functions
import PySimpleGUI as sg


todos = functions.get_todos()

enter_todo_label = sg.Text("Enter a to-do:")
message_label = sg.Text('Hello there!')
input_box = sg.InputText(tooltip='Enter a to-do:', key='todo')
add_button = sg.Button('Add')
todos_box = sg.Listbox(todos, key='selected_todo', size=(30,15), enable_events=True)
complete_button = sg.Button('Complete')
edit_button = sg.Button('Edit')

window = sg.Window('To-do App',
                   font=('Verdana', 10),
                   layout=[[enter_todo_label],
                           [input_box, add_button],
                           [message_label],
                           [todos_box, complete_button, edit_button]])

while True:
    event, values = window.read()
    print (event,values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'].capitalize() + '\n')
            functions.write_todos(todos)
            todos_box = todos_box(todos)
        case 'Complete':
            try:
                todos = functions.get_todos()
                todos.remove(values['selected_todo'][0])
                functions.write_todos(todos)
                todos_box = todos_box(todos)
            except IndexError:
                message_label.update('First select the todo from the list,\nthen press the EDIT button')
                continue
        case 'Edit':
            try:
                todos = functions.get_todos()
                todo_index = int(todos.index(values['selected_todo'][0]))
                todos[todo_index] = values['todo'].capitalize() + '\n'
                functions.write_todos(todos)
                todos_box = todos_box(todos)
            except IndexError:
                message_label.update('First select the todo from the list,\nthen type a new todo and finally press the EDIT button')
                continue
        case sg.WIN_CLOSED:
            break
    
window.close()

