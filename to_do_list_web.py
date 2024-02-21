import streamlit as st
import functions

st.title("To do app")
st.write("Minimalistic to-do app.")

for todo in functions.get_todos():
    st.checkbox(todo)
    
st.text_input('', placeholder='Add a new to do...')