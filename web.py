import streamlit as st
import functions

todos = functions.get_todos()
st.title("Welcome, to the Todo App!")
st.subheader("This app was created,")
st.write("for increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")