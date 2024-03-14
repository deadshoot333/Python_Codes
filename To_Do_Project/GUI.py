import PySimpleGUI as gui
from ToDoClass import To_Do

todo = To_Do()

label = gui.Text("Enter to do: ")
input_box = gui.InputText(tooltip="Enter a to do", key="todo")
add_button = gui.Button("Add")

list_box = gui.Listbox(
    values=todo.show(), key="show_todos", enable_events=True, size=[45, 10]
)

edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")
window = gui.Window(
    "My To-Do app",
    layout=[[label], 
            [input_box, add_button], 
            [list_box, edit_button, complete_button],
            [exit_button]],
    font=("Helvectica", 12),
)  # layout take 2D array
while True:
    event, kvalue = window.read()
    print(f"1 {event}")
    print(f"2 {kvalue}")
    match event:
        case "Add":
            guiTodo = kvalue["todo"]
            todo.add(guiTodo)
            todos = todo.show()
            window["show_todos"].update(values=todos)
        case "Edit":
            todo_to_edit = kvalue["show_todos"][0]
            new_todo = kvalue["todo"]

            todos = todo.show()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            todo.write_todo(todos)
            window["show_todos"].update(values=todos)
            print(index)
        case "Complete":
            todo_to_complete = kvalue["show_todos"][0]
            todos = todo.show()
            todos.remove(todo_to_complete)
            todo.write_todo(todos)
            window["show_todos"].update(values=todos)
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break

print("--------PROGRAMME END--------")
window.close()
