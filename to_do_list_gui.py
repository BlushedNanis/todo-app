import functions
import PySimpleGUI as sg


enter_todo_label = sg.Text("Enter a to-do:")
message_label = sg.Text('Hello there!')
input_box = sg.InputText(tooltip='Enter a to-do:', key='todo')
add_button = sg.Button('Add')
todos_box = sg.Listbox(functions.get_todos(), key = 'selected_todo',
                       size = (30,15), enable_events = True)
complete_button = sg.Button('Complete')
edit_button = sg.Button('Edit')
exit_button = sg.Button('Exit')

window = sg.Window('To-do App',
                   font=('Verdana', 10),
                   layout=[[enter_todo_label],
                           [input_box, add_button],
                           [message_label],
                           [todos_box, complete_button, edit_button],
                           [exit_button]])

while True:
    event, values = window.read()
    print (event,values)
    match event:
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
                message_label.update("First select the todo from the list,"
                                     "\nthen press the COMPLETE button")
                continue
        case 'Edit':
            try:
                todos = functions.get_todos()
                todo_index = int(todos.index(values['selected_todo'][0]))
                todos[todo_index] = values['todo'].capitalize() + '\n'
                functions.write_todos(todos)
                todos_box.update(todos)
            except IndexError:
                message_label.update("First select the todo from the list,"
                                     "\nthen type a new todo and finally"
                                     "press the EDIT button")
                continue
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
    
window.close()

