import functions
import PySimpleGUI as sg


label = sg.Text("Enter a to-do:")
input_box = sg.InputText(tooltip='Enter a to-do:')
button = sg.Button('Add')

window = sg.Window('To-do App', layout=[[label],[input_box, button]])
window.read()
window.close()

