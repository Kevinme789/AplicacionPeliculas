import flet as ft

def Appbar():
   AppBar = ft.AppBar(
        leading_width=100,
        title=ft.Text("RACEFLIX", color=ft.Colors.WHITE),
        center_title=False,
        bgcolor=ft.Colors.BLACK,
        actions=[

                ft.TextButton("Categorias",width=140,
                style=ft.ButtonStyle(color=ft.Colors.WHITE),icon=ft.Icons.CATEGORY,
                        icon_color=ft.Colors.WHITE,bottom=True,),

            ft.TextButton("Recomendadas", width=200, icon=ft.Icons.RECOMMEND, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
            ft.TextButton("Populares", width=140, icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
            ft.TextButton("Infravaloradas", icon=ft.Icons.MOOD_BAD, width=140, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
            ft.TextButton("Favoritas", width=140, icon=ft.Icons.STAR_ROUNDED, icon_color=ft.Colors.WHITE,
                          style=ft.ButtonStyle(color=ft.Colors.WHITE,)),
            ft.Text("   ", width=265),
            #ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            #ft.PopupMenuButton(
             #   items=[
              #      ft.PopupMenuItem(text="Item 1"),
               #     ft.PopupMenuItem(),  # divider
                #    ft.PopupMenuItem(
                 #       text="Checked item", checked=False
                  #  ),
                #]
            #),
        ],
    )

   return AppBar