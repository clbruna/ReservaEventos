#-*- coding: utf-8 -*-
import PySimpleGUI as sg

# Tela de Login
def loginAdmin():

    sg.theme('GreenMono')

    layout = [
        [sg.Push()],

        [sg.HSep(), sg.Image('img/loginAdmin.png'), sg.HSep()],

        [sg.Push()],

        [sg.Input(key='-LOGIN-')],

        [sg.Input(password_char='*', key='-SENHA-')],

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

# loginAdmin().read()

telaAdmin, telaNovoEvento = loginAdmin(), None

while True:

    window, events, values = sg.read_all_windows()

    if window == telaAdmin and events == sg.WIN_CLOSED:
        break

    elif window == telaAdmin and events == '-BTN_ENTRAR-':
        if values['-LOGIN-'] == 'admin' and values['-SENHA-'] == '123':
            telaNovoEvento = criarEvento()
            telaAdmin.hide()

    elif window == telaNovoEvento and events == sg.WIN_CLOSED:
        break

    elif window == telaNovoEvento and events == 'ADICIONAR':
        telaNovoEvento = criarEvento()
        telaNovoEvento.extend_layout(telaNovoEvento['-EVENTO-'],
                                     [[sg.Image('img/peca_1.png'), sg.Button('DETALHES', key='-DETALHES-')]])
        telaNovoEvento.close()

    elif events == 'REMOVER':
        janela.close()
        janela = criarEvento()