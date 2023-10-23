#-*- coding: utf-8 -*-

import PySimpleGUI as sg

"""menu = ['teste 1', 'teste 2', 'teste 3']

layout = [
    [sg.LB(menu, size=(400, 400))]
]

window = sg.Window('teste', layout)
event, values = window.read()
if event == 'Cancel':
    window.close()
"""

def login():

    layout = [
        [sg.Push(),
         sg.Text('LOGIN'),
         sg.Push()
         ],

        [sg.Text(size=(1, 1))],

        [sg.Text('Login', size=6),
         sg.Input(size=30, key='-LOGIN-')],

        [sg.Text('Senha', size=6),
         sg.Input(size=30, key='-SENHA-')],

        [sg.Push()],

        [sg.Push(),
         sg.Button('ENTRAR', key='-BTN-'),
         sg.Push()
         ],

        [sg.Push()],
    ]

    frame = [sg.Frame('teste', layout)]

    return sg.Window('Login Administrador', frame)


def menuAdm():

    layout = [

    ]


login().read()

