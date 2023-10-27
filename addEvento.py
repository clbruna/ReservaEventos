#-*- coding: utf-8 -*-
import flet as ft

def main(page: ft.Page):
    page.title = 'Menu Principal'
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos
    descricao = ft.Text('''Lorem ipsum dolor sit amet. Aut quia iure ut voluptate iure 
qui omnis amet. Ea iure consequatur qui aspernatur asperiores ab dolorem 
voluptas aut optio quia quo iure temporibus vel officiis sequi ea quam dolorem. 
Lorem ipsum dolor sit amet. Aut quia iure ut voluptate iure qui omnis amet. 
Ea iure consequatur qui aspernatur asperiores ab dolorem voluptas aut optio 
quia quo iure temporibus vel''')

    coluna1 = ft.Column(controls=[ft.Image('img/cd1.png', width=200), ft.Image('img/cd2.png', width=200), ft.Image('img/cd3.png', width=200)])
    coluna2 = ft.Column(controls=[ft.Image('img/mv1.png'), descricao], alignment=ft.MainAxisAlignment.CENTER)

    linha1 = ft.Row(controls=[coluna1, coluna2], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(linha1)
    page.update()


ft.app(target=main)





