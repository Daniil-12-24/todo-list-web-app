import streamlit as st
import funtions

todos = funtions.read_file()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    funtions.write_file(todos)


st.title('My To-do App')
st.subheader('This is my todo app!')
st.write('This app will increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a todo', placeholder='add new todo...',
              on_change=add_todo, key='new_todo')