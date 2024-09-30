import FreeSimpleGUI as fsg

label=fsg.Text('Add To-Do App')
input=fsg.InputText(tooltip='Enter To-Do Item')
button=fsg.Button('Add')
 
window=fsg.Window('My To-Do App', layout=[[label],[input, button]])
window.read()
window.close()
