import PySimpleGUI as gui
from ToDoClass import To_Do
import time

gui.theme("DarkPurple4")
todo = To_Do()

clock=gui.Text('clk',key='clock')
label = gui.Text("Enter to do ")
input_box = gui.InputText(tooltip="Enter a to do", key="todo")
add_button = gui.Button("Add",size=20)

list_box = gui.Listbox(
    values=todo.show(), key="show_todos", enable_events=True, size=[45, 10]
)

edit_button = gui.Button("Edit",size=15)
complete_button = gui.Button("Complete",size=15)
exit_button = gui.Button("Exit")
window = gui.Window(
    "My To-Do app",
    layout=[[label],
            [input_box, add_button], 
            [list_box, edit_button,complete_button,exit_button], 
            [clock]],
    font=("Helvectica", 12),
)  # layout take 2D array
while True:
    event, kvalue = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(f"1 {event}")
    print(f"2 {kvalue}")
    match event:
        case "Add":
            guiTodo = kvalue["todo"]
            todo.add(guiTodo)
            todos = todo.show()
            window["show_todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = kvalue["show_todos"][0]
                new_todo = kvalue["todo"]

                todos = todo.show()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                todo.write_todo(todos)
                window["show_todos"].update(values=todos)
                print(index)
            except IndexError:
                gui.popup("Please select an Item first",font=("Helvectica",12))
        case "Complete":
            try:
                todo_to_complete = kvalue["show_todos"][0]
                todos = todo.show()
                todos.remove(todo_to_complete)
                todo.write_todo(todos)
                window["show_todos"].update(values=todos)
            except IndexError:
                gui.popup("Please select an Item First",font=("Helvectica",12))
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break

print("--------PROGRAMME END--------")
window.close()
