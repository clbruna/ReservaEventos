#-*- coding: utf-8 -*-

import flet as ft
from elementos import *



def main(page: ft.Page):

    page.bgcolor = ft.colors.GREY
    page.title = 'Menu Principal'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    ############# Elementos #############

    # Cabeçalho Janela
    cabecalhoPrincipal = ft.Container(
        ft.Row(controls=[
            ft.Container(ft.Text('EVENTOS DISPONÍVEIS TESTE', color=ft.colors.WHITE, width=700, height=60)),
            ft.IconButton(icon=ft.icons.SETTINGS, width=100, height=60, icon_color=ft.colors.WHITE, icon_size=40)
        ], width=1300, height=90, alignment=ft.MainAxisAlignment.SPACE_AROUND, vertical_alignment=ft.CrossAxisAlignment.CENTER), bgcolor='BLACK', border_radius=30
    )

    # Cabeçalho
    cabecalho_detalhesEvento = ft.Row(controls=[
        ft.Column(controls=[
            ft.Text('MOODSWINGS IN THIS ORTHER', color=ft.colors.WHITE), ft.Text('LANÇAMENTO: 11/03/2021', color=ft.colors.WHITE)
        ], height=60),
        btnDetalhes
    ], width=720, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


    # Detalhes do Evento
    detalhesEvento = ft.Container(
        ft.Column(controls=[
            cabecalho_detalhesEvento,
            ft.Container(ft.Image('img/mv1.png'), border_radius=20),
            ft.Text(texto, color=ft.colors.WHITE, width=720)
        ], height=550, alignment=ft.MainAxisAlignment.SPACE_AROUND, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=ft.colors.BLACK, width=820, border_radius=30
    )

    # Menu Lateral
    menuLateral_1 = ft.Column(controls=[
        ft.Container(ft.Image('img/cd1.png'), bgcolor='black', width=280, height=160, border_radius=30),
        ft.Container(ft.Image('img/cd2.png'), bgcolor='black', width=280, height=160, border_radius=30, opacity=.8),
        ft.Container(ft.Image('img/cd3.png'), bgcolor='black', width=280, height=160, border_radius=30, opacity=.8)
    ], height=550, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


    menuLateral_2 = ft.Column(controls=[
        ft.Image('img/cd1.png', width=130),
        ft.Image('img/cd2.png', width=130, opacity=0.1),
        ft.Image('img/cd3.png', width=130, opacity=0.1)
    ], height=550, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, horizontal_alignment=ft.CrossAxisAlignment.START)


    tela = ft.Row(controls=[menuLateral_1, detalhesEvento], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    telaTeste = ft.Column(controls=[
        cabecalhoPrincipal,
        tela
    ])

    tela3 = ft.Column(controls=[
        ft.Row(controls=[cabecalhoPrincipal])
    ])

    window = ft.Column(controls=[cabecalhoPrincipal, tela])


    page.add(window)
    page.update()


ft.app(target=main)
