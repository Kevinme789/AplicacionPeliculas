import flet as ft

from flet.core import page

import AppBar
import Pasarela


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.title = "RaceFlix"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT


    # INICIO DE APPBAR--------------------------------------
    page.appbar = AppBar.Appbar()
    # FINAL DE APPBAR---------------------------------------

    page.add(Pasarela.Pasarela())

    page.update()
ft.app(target=main)