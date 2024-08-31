FILEPATH =f"Files/todos.txt"

def get_todos(filepath=FILEPATH):#definicja własnej funkcji - po to by nie dublować kod w aplikacji z przypisaniem defaultowego parametru
    """ Read the text file and return the list of to-do items""" #wyskoczy jeśli wpiszemy print(help(get_todos))
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # z with content manager nie musimy pamiętać o zamknięciu pliku
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        print(f"{todos_arg} z functions.write_todos")
        file.writelines(todos_arg)

if __name__ == "__main__": #__name__ sie zmienia w zależności od tego skąd jest wywoływany plik functions. bedzie rowny main tylko jeśli odplamy go bezpośrdenio
    print("Hello from functions")