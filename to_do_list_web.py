import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo'].capitalize()
    if todo == '':
        return
    else:
        todos=functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)
        st.session_state['new_todo'] = ''
    
def complete_todos():
    new_todos = functions.get_todos()
    for index, todo in enumerate(functions.get_todos()):
        if st.session_state[index] == True:
            new_todos.remove(todo)
    functions.write_todos(new_todos)


st.title("To do app")
st.write("Minimalistic to-do app.")

st.divider()

for index, todo in enumerate(functions.get_todos()):
    st.checkbox(todo, key=index)

st.divider()

st.text_input('Todo entry', label_visibility='hidden', 
              placeholder='Add a new to do...',
              on_change=add_todo, key='new_todo')

st.button('Complete', key='complete',
          on_click=complete_todos)
st.session_state