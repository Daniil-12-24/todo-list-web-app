import streamlit as st
import funtions

todos = funtions.read_file()

st.title('My To-do App')
st.subheader('This is my todo app!')
st.write('This app will increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Enter a todo', placeholder='add new todo...')