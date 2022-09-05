from PySimpleGUI import PySimpleGUI as sg
import sqlite3 as lite
con = lite.connect('bank.db')
import main

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Name'),sg.Input(key='name', size=(20,1))],
    [sg.Text('Age'),sg.Input(key='age', size=(20,1))],
    [sg.Text('Category'),sg.Input(key='category', size=(20,1))],
    [sg.Button('Submit'),sg.Button('Show Users')]
    ]
#Window
window = sg.Window('Register', layout)

# Actions
while True:
    events, value = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Show Users':
        text = 'age'
    if events == 'Submit':
        text = 'name'
        if text == '':
            print('Null string')
        else:
            try:
                value = int(text)
                print(f'Your age: {value}')
                if value >= 18:
                    print('Adult')
                else:
                    print('Child')
            except:
                print("Not a age")