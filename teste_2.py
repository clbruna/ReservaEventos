#-*- coding: utf-8 -*-
import PySimpleGUI as sg

# Tela de Login
def loginAdmin():

    sg.theme('GreenMono')

    layout = [
        [sg.Push()],

        [sg.HSep(), sg.Image('img/loginAdmin.png'), sg.HSep()],

        [sg.Push()],

        [sg.Input('Usuário', key='-LOGIN-')],

        [sg.Input('Senha', key='-SENHA-')],

        [sg.Push(), sg.Button('ENTRAR', key='-BTN_ENTRAR-'), sg.Push()],

        [sg.Push()]

    ]

    return sg.Window('Acesso Restrito', layout=layout, finalize=True)



# Criando o layout
def criarEvento():

    sg.theme('GreenMono')

    evento = [

    ]

    layout = [
        [sg.Frame('', layout=evento, key='-EVENTO-')],
        [sg.Button('ADICIONAR'), sg.Button('REMOVER')]
    ]

    return sg.Window('Gerenciador de Eventos', layout=layout, finalize=True)


# Criando a janela
janela = criarEvento()

loginAdmin().read()

while True:

    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'ADICIONAR':
        janela.extend_layout(janela['-EVENTO-'],
                             [[sg.Image('img/peca_1.png'), sg.Button('DETALHES', key='-DETALHES-')]])

    elif event == 'REMOVER':
        janela.close()
        janela = criarEvento()