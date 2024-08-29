""" GUI do aplikacji To do"""
import functions
import FreeSimpleGUI as sg

label =sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo",key="todo") #możemy dodawać własne klucze-  bez tego key wartość przypisywana kolejne. Pierwszy element ma 0
add_button = sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(), key='todos',
                    enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',10)) #lista FreeSimpleGUI widgetów
while True:
    event, values = window.read() #wyświetla obiekty w GUI. Mozna od razu przypisywać wartość do więcej niż jednej zmiennej
    #korzystamy z tego, że do listy albo tuple można przypisać od razu kilka zmiennych
    """print(f"event = {event}")
    print(type(event))
    print(f"values = {values}")
    print(type(values))
    print(type(values['todo']))
    print(type(values['todos']))"""
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"#przypisujemy do new_todo element krotki z kluczem 'todo' - czyli to co wpiszemy w gui
            todos.append(new_todo)
            functions.write_todos(todos) #zapisujemy zaktualizowaną listę do pliku
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit=values['todos'][0]
            #print(todo_to_edit)
            new_todo = values['todo']
            todos =functions.get_todos()
            index_to_edit = todos.index(todo_to_edit)
            todos[index_to_edit]= new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            #input_box.update(values['todos'][0])
            #alternative way
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break #wychodzimy z pętli while jeśli ktoś zamknał okno programu
            #zamiast break można użyć też funckji exit() - wbudowana funkcja pythona kończąca natychmiast pracę programu
window.close()#zamyka obiekty w GUI