""" GUI do aplikacji To do"""
import functions
import FreeSimpleGUI as sg
import time
import os

#kawałek kodu tworzący folder Files i plik todos w nim
if not os.path.exists(f"Files/todos.txt"):
    os.mkdir("Files")
    with open("Files/todos.txt", 'w') as file:
        pass #nic nie rób

sg.theme("NeonBlue1")

labelClock =sg.Text("", key = "clock")
label =sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo",key="todo", size =47) #możemy dodawać własne klucze-  bez tego key wartość przypisywana kolejne. Pierwszy element ma 0
add_button = sg.Button ("Add",size=10,  mouseover_colors="LightBlue2", tooltip="Add", key="Add")
#użycie obrazka zamiast napisu na przycisku
#add_button = sg.Button (size=10, image_source="add.png",button_color="LightBlue2", mouseover_colors="LightBlue2", tooltip="Add", key="Add")
list_box=sg.Listbox(values=functions.get_todos(), key='todos',
                    enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[
                           [labelClock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',10)) #lista FreeSimpleGUI widgetów
while True:
    event, values = window.read(timeout=900) #wyświetla obiekty w GUI. Mozna od razu przypisywać wartość do więcej niż jednej zmiennej
    #window["clock"].update(value=time.strftime("%b %d, %Y- %H:%M:%S"))
    #korzystamy z tego, że do listy albo tuple można przypisać od razu kilka zmiennych
    """print(f"event = {event}")
    print(type(event))
    print(f"values = {values}")
    print(type(values))
    print(type(values['todo']))
    print(type(values['todos']))"""
    if event == sg.WINDOW_CLOSED:
        break
        window.close()
    elif event == "Add":
            #print(f"Add start ...")
            #print(f"1. todos before get_todos()  {values}")
            todos = functions.get_todos()
            #print(f"2. todos after get_todos()  {todos}")
            new_todo = values['todo']+"\n"#przypisujemy do new_todo element krotki z kluczem 'todo' - czyli to co wpiszemy w gui
            #print(f"3. new todo  {new_todo} from values['todo'] {values['todo']}")
            todos.append(new_todo)
            #print(f"4. todos after append new_todo {todos}")
            functions.write_todos(todos) #zapisujemy zaktualizowaną listę do pliku
            window['todos'].update(values=todos)
            #print(f"Add end ...")
    elif event == "Edit":
            try:
                #print(f"Edit start ...")
                #print(f"1. Edit values['todos'][0]  {values['todos'][0]}")
                todo_to_edit=values['todos'][0]
                #print(f"2. Edit todo_to_edit  {todo_to_edit}")
                new_todo = values['todo']
                if(len(new_todo.splitlines())==1):
                    new_todo=new_todo+'\n'
                else:
                    pass
                #print(f"3. Edit new_todo  {new_todo}")
                todos =functions.get_todos()
                #print(f"4. Edit todos  {todos}")
                index_to_edit = todos.index(todo_to_edit)
                #print(f"5. Edit todos  {todo_to_edit} {index_to_edit}")
                todos[index_to_edit]= new_todo
                #print(f"6. todos after edition  {todos}")
                functions.write_todos(todos)
                #print(f"7. todos after write  {todos}")
                window['todos'].update(values=todos)
                #print(f"Edit end ...")
            except IndexError:
                print("Please select an item first")
                sg.popup("Please select an item first", font=('Helvetica', 15))
    elif event == "todos":
            #input_box.update(values['todos'][0])
            #alternative way
            window['todo'].update(value=values['todos'][0].rstrip()) #dodałem rstrip by przy edycji zadania nie dodawać niepotrzebne \n
    elif event == "Complete":
            try:
                #print(f"Complete start ...")
                #print(f"1. todo_to_complete {values['todos']}")
                todo_to_complete = values['todos'][0]
                #print(f"2. todo_to_complete {values['todos'][0]}")
                #print(f"3. todo_to_complete = {todo_to_complete}")
                todos = functions.get_todos()
                #print(f"4. todos = {todos}")
                todos.remove(todo_to_complete)
                #print(f"5. todos after removal = {todos}")
                functions.write_todos(todos)
                #print(f"6.todos after write = {todos}")
                window['todos'].update(values=todos)
                window['todo'].update(value='')
                #print(f"Complete end ...")
            except IndexError:
                print("Please select an item first")
                sg.popup("Please select an item first", font=('Helvetica', 15))
    elif event == 'Exit':
            break
            window.close()
    window["clock"].update(value=time.strftime("%b %d, %Y- %H:%M:%S"))


            #wychodzimy z pętli while jeśli ktoś zamknał okno programu
        # #zamiast break można użyć też funckji exit() - wbudowana funkcja pythona kończąca natychmiast pracę programu
window.close()#zamyka obiekty w GUI