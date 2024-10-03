import streamlit as st
import functions

def add_todo():
    new_todo=st.session_state['new_todo'] + '\n'
    todos.append(new_todo) 
    functions.write_todos(todos)
    
todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is a sample todo app')
st.write('This is to manage productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()
        
        
        
st.text_input(label='random', placeholder='Add new todo', on_change=add_todo, key='new_todo',label_visibility='hidden')

st.session_state