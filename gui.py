import FreeSimpleGUI as fsg
import functions


label=fsg.Text('Add To-Do App')
input=fsg.InputText(tooltip='Enter To-Do Item', key='to-do')
button=fsg.Button('Add')
 
window=fsg.Window('My To-Do App', 
                  layout=[[label],[input, button]], 
                  font=('Helvetica', 16)
                  )
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
        case fsg.WIN_CLOSED:    
            break
window.close()  
