# from functions import functions.get_todos, functions.write_todos
import functions
import time
now = time.strftime('%B %d, %Y %H:%M:%S')
print('It is currently', now)
while True:
    user_action=input('Type add, remove, show, edit or quit:')
    user_action=user_action.strip()
 
    if user_action.startswith('add') or user_action.startswith('new'):
       
        todo=user_action[4:]
        todos=functions.get_todos('todos.txt')
        todos.append(todo.title() + '\n')
        functions.write_todos('todos.txt',todos)    
        
    elif user_action.startswith('show') or user_action.startswith('display'):
       
        todos=functions.get_todos('todos.txt')
        for index, item in enumerate(todos):
            item=item.strip('\n')
            print(f"{index+1}-{item}")
                      
    elif user_action.startswith('edit'):
        
        number=int(user_action[5:])
        todos=functions.get_todos('todos.txt')

        new_todo=input('Enter the new todo:')
        todos[number-1]=new_todo + '\n' 
        
        print('Todo has been updated')
        functions.write_todos('todos.txt',todos)  
    elif user_action.startswith('remove'):
        
        number=int(user_action[7:])
        todos=functions.get_todos('todos.txt')
        todo_to_remove=todos[number-1].strip('\n')
        todos.pop(number-1)
        
        functions.write_todos('todos.txt',todos)
            
        print(f'{todo_to_remove} has been removed')
       
    elif user_action.startswith('quit') or user_action.startswith('exit'):
        break
    
    else:
        print('Unacceptable input, please enter something from the options that are mentioned above')
        continue
    
print('Toodaloo!')
