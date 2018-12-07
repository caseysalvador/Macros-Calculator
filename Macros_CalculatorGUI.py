import sys, PySimpleGUI as sg

layout = [[sg.Text('Protein:'), sg.Text('', key='_OUTPUT_') ],
        [sg.Text('Fat:'), sg.Text()]
            ]]

window = sg.Window('Macros Calculator').Layout(layout)