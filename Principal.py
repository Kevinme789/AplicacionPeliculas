import flet as ft
from flet import IconButton, Page, Row, TextField, icons
def main(page: Page):
    page.title = "RaceFlix"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    txt = TextField(value = "hola", text_align="left", width=100)
    txt2 = TextField(value = " hola", text_align="left", width=100)
    def check(e):
            e.control.checked = not e.control.checked
            page.add(txt)
            txt.value = txt.value + txt2.value
            page.update()
    def xd(event):
        page.add(txt)
        page.update()
        pass

  # INICIO DE APPBAR ---------------------------------------------
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.LOCAL_MOVIES),
        leading_width=100,
        title=ft.Text("RACEFLIX",color=ft.Colors.BLACK),
        center_title=False,
        bgcolor=ft.Colors.BLUE_GREY_100,
        actions=[

            ft.TextButton("Recomendadas", width=200,icon=icons.RECOMMEND, icon_color=ft.Colors.BLUE_GREY_900,style=
            ft.ButtonStyle(color=ft.Colors.BLUE_GREY_900),on_click=xd),
            ft.TextButton("Favoritas", width=140,icon=icons.STAR_ROUNDED,icon_color=ft.Colors.BLUE_GREY_900,style=
            ft.ButtonStyle(color=ft.Colors.BLUE_GREY_900)),
            ft.TextButton("Categorias", width=140,icon=icons.CATEGORY,icon_color=ft.Colors.BLUE_GREY_900,style=
            ft.ButtonStyle(color=ft.Colors.BLUE_GREY_900)),
            ft.TextButton("Populares",width=140,icon=icons.FAVORITE,icon_color=ft.Colors.BLUE_GREY_900,style=
            ft.ButtonStyle(color=ft.Colors.BLUE_GREY_900)),
            ft.TextButton("Infravaloradas",icon=icons.MOOD_BAD,width=140,icon_color=ft.Colors.BLUE_GREY_900,style=
            ft.ButtonStyle(color=ft.Colors.BLUE_GREY_900)),
            ft.Text("   ",width=140),


            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check
                    ),
                ]
            ),
        ],
    )
    #FINAL DE APPBAR---------------------------------------


    # INICIO BODY-------------------------------------------------------



    page.add()
ft.app(target=main)
