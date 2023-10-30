#-*- coding: utf-8 -*-

import flet as ft

texto = 'Lorem ipsum dolor sit amet. Aut quia iure ut voluptate iure qui omnis amet. Ea iure consequatur qui aspernatur asperiores ab dolorem voluptas aut optio quia quo iure temporibus vel officiis sequi ea quam dolorem. Lorem ipsum dolor sit amet. Aut quia iure ut voluptate iure qui omnis amet. Ea iure consequatur qui aspernatur asperiores ab dolorem voluptas aut optio quia quo iure temporibus vel'

btnDetalhes = ft.ElevatedButton(
    'DETALHES', style=ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.FOCUSED: ft.colors.LIGHT_BLUE_ACCENT_100,
            ft.MaterialState.DEFAULT: ft.colors.WHITE,
        },
        bgcolor={ft.MaterialState.FOCUSED: ft.colors.BLACK, '': ft.colors.CYAN_800, ft.MaterialState.HOVERED: ft.colors.CYAN_600}
    ), width=150, height=60

)


