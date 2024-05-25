import streamlit as st
import functions


def add_todo():
    """
    Catch user input if there is any to add it to the todos.txt.
    If there isn't a new input then it will do nothing.
    """
    todo = st.session_state['new_todo'].capitalize()
    if todo == '':
        return
    else:
        todos=functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)
        st.session_state['new_todo'] = ''
    
def complete_todos():
    """
    Removes the marked todo by the user from todos.txt
    """
    new_todos = functions.get_todos()
    for index, todo in enumerate(functions.get_todos()):
        if st.session_state[index] == True:
            new_todos.remove(todo)
    functions.write_todos(new_todos)
    st.balloons()
    
def priority_mark():
    """
    Marks an existent to-do as priority (red color)
    """
    marked_todos = functions.get_todos()
    for index, todo in enumerate(functions.get_todos()):
        if st.session_state[index] == True:
            todo = todo.strip('\n')
            marked_todos[index] = (f":red[{todo}]:exclamation:\n")
    functions.write_todos(marked_todos)
    
def normal_mark():
    """
    Marks an existent to-do as normal (standard color)
    """
    normal_todos = functions.get_todos()
    for index, todo in enumerate(functions.get_todos()):
        if st.session_state[index] == True:
            todo = todo.split(']')
            normal_todos[index] = (todo[0][5:] + '\n')
    functions.write_todos(normal_todos)

# Set Web-app body
st.title("To do app")
st.write("Minimalistic to-do app.")

st.divider()

for index, todo in enumerate(functions.get_todos()):
    st.checkbox(todo, key=index)

st.divider()

st.text_input('Todo entry', label_visibility='hidden', 
              placeholder='Add a new to do...',
              on_change=add_todo, key='new_todo')

col1, col2 , col3 = st.columns([2, 1, 1])
with col1:
    st.button('Complete	:white_check_mark:', key='complete',
            on_click=complete_todos)
with col2:
    st.button(':red[Mark as pripority]'
              ':heavy_exclamation_mark:',
              key='priority', on_click=priority_mark)
with col3:
    st.button('Mark as normal:grey_exclamation:',
              key='normal', on_click=normal_mark)

st.caption("_Made by BlushedNanis_ :copyright:")