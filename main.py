import PySimpleGUI as sg
from cpf_validator import search_cpf

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Search CPF (Only Numbers)'), sg.InputText()],
            [sg.Button('Search'), sg.Button('Exit')] ]

# Create the Window
window = sg.Window('CPF VALIDATOR', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    cpf_output = search_cpf(values[0])

    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    print(f'({values[0]}) =====> {cpf_output}')

window.close()
