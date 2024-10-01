import FreeSimpleGUI as fsg
import functions


label=fsg.Text('Add To-Do App')
input=fsg.InputText(tooltip='Enter To-Do Item', key='to-do')
add_button=fsg.Button('Add')
list_box=fsg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=(50,10)
                     )
#gets the list of existing todos from the file

edit_button=fsg.Button('Edit')
complete_button=fsg.Button('Complete')
exit_button=fsg.Button('Exit') 
 
window=fsg.Window('My To-Do App', 
                  layout=[[label],
                          [input, add_button], 
                          [list_box, edit_button, complete_button],
                          [exit_button]
                          ], 
                  font=('Helvetica', 16)
                  )
# this "window" is the parent instance that contains information from all previous instances
# the layout is a list of lists, each list is a row of the window

while True:
    event, values= window.read() 
    #event get the value of the button's name, i.e. 'Add' in this case.
    #Values get the value of the "key" argument of the InputText method, i.e. 'to-do' in this case.
    
    print(event)
    print(values)
    
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['to-do'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos) 
            # windows['todos'] is the listbox and gets the argument from the key ofr Listbox defined earlier
        
        case 'Edit':
            todo = values['todos']#gets the selected todo
            todo_to_edit = todo[0]
            #gets the first item in the list, as "values" is a dictionary where each value is a list in itself
             
            new_todo = values['to-do'] + '\n'
            
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos) 
            # windows['todos'] is the listbox and gets the argument from the key ofr Listbox defined earlier
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos=functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['to-do'].update(value='')
# this line is important because even after removing an item from the listbox,  
# the input text box will still show the removed item. Thgis line will clear the input text box
            
        
        case 'Exit':
            break
        case 'todos':
            todo = values['todos']
            window['to-do'].update(value=todo[0])
            #updates the input text with the selected todo 
        case fsg.WIN_CLOSED:    
            break
        
window.close()  
