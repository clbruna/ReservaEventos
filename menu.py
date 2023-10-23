#-*- coding: utf-8 -*-

import PySimpleGUI as sg

texto = '''     Lorem ipsum dolor sit amet. Aut quia iure ut voluptate iure 
qui omnis amet. Ea iure consequatur qui aspernatur asperiores ab dolorem 
voluptas aut optio quia quo iure temporibus vel officiis sequi ea quam dolorem. 
Lorem ipsum dolor sit amet. Aut quia iure ut voluptate iure qui omnis amet. 
Ea iure consequatur qui aspernatur asperiores ab dolorem voluptas aut optio 
quia quo iure temporibus vel'''

def menuPrincipal():

    layout = [
        [sg.Push(), sg.Text('Menu Principal'), sg.Push()],

        [sg.HSep()], [sg.Text()],

        [sg.Push(), sg.Image('img/peca_1.png'), sg.Push()],
        [sg.Text(size=(10, 1))],
        [sg.Text(size=24), sg.Text('Título: Apresentação\nData: 17/10/2023'), sg.Push(), sg.Button('DETALHES', size=(20, 2)), sg.Text(size=24)],

        [[sg.Text()], sg.HSep()], [sg.Text()],

        [sg.Push(), sg.Image('img/peca_1.png'), sg.Push()],
        [sg.Text(size=(10, 1))],
        [sg.Text(size=24), sg.Text('Título: Apresentação\nData: 17/10/2023'), sg.Push(), sg.Button('DETALHES', size=(20, 2)), sg.Text(size=24)],

        [[sg.Text()], sg.HSep()], [sg.Text()]
    ]

    return sg.Window('Menu Principal', layout, size=(850, 500))


teste_frame = []

def detalhes():

    layout = [
        [
            sg.Push(),
            sg.Text('TÍTULO', justification='center'),
            sg.Push()

        ],



        [
            sg.Push(),
            sg.Image('img/peca_1.png'),
            sg.Push()
        ],

        [
            sg.Text()
        ],

        [
            sg.Text(size=5),
            sg.Frame('teste', [teste_frame]),
            #sg.Text(texto, justification='left'),
            sg.Text(size=5)
        ],

        [sg.Text()],

        [
            sg.Push(),
            sg.Button('RESERVAR', size=(15, 2)),
            sg.Push()
        ]

    ]

    return sg.Window('Detalhes', layout)


detalhes().read()

