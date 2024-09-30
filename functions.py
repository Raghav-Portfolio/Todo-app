def get_todos(filepath):
    with open(filepath,'r') as file:
        todos_local=file.readlines()
    return todos_local

def write_todos(filename,todos_write):
        with open(filename,'w') as file:
            file.writelines(todos_write)