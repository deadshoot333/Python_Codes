def get_todos(filepath="To_Do_Project/ToDos.txt"):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(filepath="To_Do_Project/ToDos.txt"):
    with open(
        filepath, "r"
    ) as file:  ##with context manager is more efficent then file open() and close()
        todos = file.readlines()


while True:
    user_action = input("Enter add,show,edit,complete or exit: ")
    user_action = user_action.strip()  ##removes any whitespace from input
    if user_action.startswith("add"):

        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        with open("To_Do_Project/ToDos.txt", "a") as file:
            file.write(todo)

    elif user_action.startswith("show"):

        # edited_todos=[item.strip('\n') for item in todos]  #list comprehension
        for index, item in enumerate(
            todos
        ):  # using enumerate  function we can print with index number in the list
            item = item.strip("\n")
            print(f"{index+1}. {item}")

    elif user_action.startswith("edit"):
        number = int(input("Enter the task number to be edited: "))
        number = number - 1
        with open("To_Do_Project/ToDos.txt", "r") as file:
            todos = file.readlines()
        new_task = input("Enter the todo: ")
        todos[number] = new_task + "\n"
        with open("To_Do_Project/ToDos.txt", "w") as file:
            file.writelines(todos)
    elif user_action.startswith("complete"):
        number = int(input("Enter the task number to be completed: "))
        with open("To_Do_Project/ToDos.txt", "r") as file:
            todos = file.readlines()
        todos.pop(number - 1)
        with open("To_Do_Project/ToDos.txt", "w") as file:
            file.writelines(todos)
    elif user_action.startswith("exit"):
        break

print("-------END-------")
