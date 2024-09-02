import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Welcome, to the Todo App!")
st.subheader("This app was created,")
st.write("for increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun() # this is needed for checkboxes

st.text_input(label="Please, enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new todo")

# st.session_state 