import streamlit as st
import functions as func


todos = func.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)


todos = func.get_todos()
st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")

# Add checkbox
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# Add text box
st.text_input(label="Can't be empty", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")
