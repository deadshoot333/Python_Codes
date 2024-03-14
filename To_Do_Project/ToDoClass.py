class To_Do:
    def __init__(self):
        self.__todos = []

    @property
    def todos(self):
        return self.__todos

    def add(self, add_todo, filepath="To_Do_Project/ToDos.txt"):
        with open(filepath, "r") as file:
            self.__todos = file.readlines()
        self.__todos.append(add_todo + "\n")
        with open(filepath, "w") as file:
            file.writelines(self.__todos)

    def show(self, filepath="To_Do_Project/ToDos.txt"):
        with open(filepath, "r") as file:
            self.__todos = file.readlines()
        return self.__todos
        # for index, item in enumerate(self.__todos):
        #     item = item.strip("\n")
        #     print(f"{index+1}. {item}")

    def edit(self, filepath="To_Do_Project/ToDos.txt"):
        number = int(input("Enter todo number you want to edit: "))
        with open(filepath, "r") as file:
            self.__todos = file.readlines()
        edited_todo = input("Enter the todo: ")
        self.__todos[number - 1] = edited_todo
        with open(filepath, "w") as file:
            file.writelines(self.__todos)

    def complete(self, filepath="To_Do_Project/ToDos.txt"):
        number = int(input("Enter the task number to be completed: "))
        with open(filepath, "r") as file:
            self.__todos = file.readlines()
        self.__todos.pop(number - 1)
        with open("To_Do_Project/ToDos.txt", "w") as file:
            file.writelines(self.__todos)

    def write_todo(self,todo_list,filepath="To_Do_Project/ToDos.txt"):
        with open(filepath, "w") as file:
            file.writelines(todo_list)


# td = To_Do()
# print(td.todos)
# while True:
#     action = input("Enter add,show,complete,edit or exit: ")
#     action = action.strip()
#     if action == "add":
#         add_todo = input("Enter a todo: ")
#         td.add()
#     elif action == "show":
#         td.show()
#     elif action == "complete":
#         td.complete()
#     elif action == "edit":
#         td.edit()
#     elif action == "exit":
#         print("-------END--------")
#         break
#     else:
#         print("Invalid option")
