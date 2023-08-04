import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write(" This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun() # may only need rerun

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')



# streamlit
# it's enough to just call the functions above (lines 6-8) in the order
# you want them to appear on the page

# when the user reloads/refresh the page the python code is re executed
# when the web app is public it can have many users at the same time.
# each user will have a different view - the code is executed separately
# for each user. The CPU of the webserver is going to handle that request.
# It's important to have sufficient hardware (RAM and CPU) to handle many users at once.
# there are good options that are scalable and you can increase RAM and CPU when user numbers increase.


# when the user enters a todo and presses enter - the function is called and the list updates
# with the new todo.
# then the lines of code below 17 -18 the checkbox and new todo are added.

# how to run web app

# run this line in the pycharm terminal: streamlit run web.py
# you can stop it running with: ctrl 'c' in the terminal

# to deploy on the web, you need to make sure that you have just the
# essential files in the project so we:
## > file > new project > named: web_app1 and virtual environment checked
## > create > open in new window
## delete the main.py and copy and paste the files from the old project
## install the relevant packages - streamlit only needed here
## check it all runs

# to deploy you need a requirements.txt file to go with the code so that
# python installed in the web can use your code - run this in the terminal
# pip freeze > requirements.txt to set up the file (it automatically writes the
# 3rd party packages to the txt file.
# pip freeze on it's own writes the packages in the command line.


