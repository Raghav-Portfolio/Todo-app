FILEPATH='todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
        todos_local=file.readlines()
    return todos_local

def write_todos(todos_write,filename=FILEPATH):
        with open(filename,'w') as file:
            file.writelines(todos_write)