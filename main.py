from functions import get_todos, write_todos #import funkcji i procedur
# mozna też wpisać improt functions, ale tedy przed wywołaniem funkcji musimy podac prefiks function. np functions.get_todos()

while True:
    user_action=input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() #usuwamy białe elementy z wprowadzonej inpitu usera

    if user_action.startswith("add"):#if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]+"\n"#list slicing
        if(len(todo)<3):
            todo=input("Enter some meaningfull task here: ")+"\n"
            print("adding")
        else:
            print("adding")

        todos=get_todos() #mozna podawać wprost parametr do którego przypisujemy argument (filepath=f"../../Files/todos.txt") albo nic nie pisać i zostanie
                        # uzyty defaultowy parametr

        todos.append(todo)

        write_todos(todos,f"../../Files/todos.txt")


    elif user_action.startswith("show"):#'show'in user_action:

        todos=get_todos(f"../../Files/todos.txt")

        new_todos=[item.strip('\n') for item in todos]

        for index,item in enumerate(new_todos):
            #mozna też tutaj, przed przekazaniem item dalej usunąć z niego '\n'
            row=f"{index+1}-{item}" #f-string -- f""
            print(row)

    elif user_action.startswith("edit"):#elif 'edit'in user_action:
        try:
            number=int(user_action[5:])#int(input("Enter a number of todo to edit: "))
            number=number-1

            todos=get_todos()#nie musimy podawać żadnego argumentu

            new_todo =input("Enter new todo: ")
            todos[number]=new_todo+"\n"

            write_todos(todos)#nie musimy podawać drugiego argumentu, który nie ma wartości defaultowej

        except ValueError:
            print("Your command is not valid.")
            continue #ignoruje wszystko co jest poniżej i wraca na poczatek bloku - w tym przypadku try

    elif user_action.startswith("complete"):
        try:
        #elif  "complete" in user_action:
            number =int(user_action[9:]) #int(input("Enter a number of todo to complete : "))
            index = number - 1

            todos=get_todos()

            todo_to_remove=todos[index]
            todos.pop(index)

            write_todos(todos)

            message =f"Todo '{todo_to_remove.strip()}' was removed from the list"
            print(message)
        except IndexError:
            print ("There is no item with such number")
        except ValueError:
            print("Please enter a number")
    elif user_action.startswith("exit"):
    #elif 'exit' in user_action:
        break #wyjście z pętli
    else:
        print("Command not valid")

print ("Bye!")
