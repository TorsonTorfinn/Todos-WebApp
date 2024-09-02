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

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new todo")

st.session_state