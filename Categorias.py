import flet as ft
from flet.core.icons import icons
from flet.core.types import MainAxisAlignment, TextAlign

import AppBar


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.appbar = AppBar.Appbar()

    categoria = ft.Column(
        controls=[
            ft.Text("Categorias",size=50,color=ft.Colors.WHITE),
        ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Comedia", color=ft.Colors.WHITE, size=30,
                                                  text_align=TextAlign.RIGHT),
                                    ft.Icon(ft.Icons.THEATER_COMEDY,color=ft.Colors.WHITE),
                                ],alignment=MainAxisAlignment.CENTER,),

                            ft.Image(src="imagenes/arania0.jpg",width=400,height=450,),
                        ]
                    ),
                    width=400,
                    height= 500,
                ),
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Romance", color=ft.Colors.WHITE, size=30,
                                            text_align=TextAlign.RIGHT),
                                    ft.Icon(ft.Icons.HEART_BROKEN, color=ft.Colors.WHITE),
                                ], alignment=MainAxisAlignment.CENTER, ),

                            ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                        ]
                    ),
                    width=400,
                    height=500,
                ),
                ft.Container(
                    bgcolor=ft.Colors.TRANSPARENT,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Romance", color=ft.Colors.WHITE, size=30,
                                            text_align=TextAlign.RIGHT),
                                    ft.Icon(ft.Icons.HEART_BROKEN, color=ft.Colors.WHITE),
                                ], alignment=MainAxisAlignment.CENTER, ),

                            ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                        ]
                    ),
                    width=400,
                    height=500,
                )
            ],alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
            ft.Row(
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Comedia", color=ft.Colors.WHITE, size=30,
                                                text_align=TextAlign.RIGHT),
                                        ft.Icon(ft.Icons.THEATER_COMEDY, color=ft.Colors.WHITE),
                                    ], alignment=MainAxisAlignment.CENTER, ),

                                ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                            ]
                        ),
                        width=400,
                        height=500,
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Romance", color=ft.Colors.WHITE, size=30,
                                                text_align=TextAlign.RIGHT),
                                        ft.Icon(ft.Icons.HEART_BROKEN, color=ft.Colors.WHITE),
                                    ], alignment=MainAxisAlignment.CENTER, ),

                                ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                            ]
                        ),
                        width=400,
                        height=500,
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Romance", color=ft.Colors.WHITE, size=30,
                                                text_align=TextAlign.RIGHT),
                                        ft.Icon(ft.Icons.HEART_BROKEN, color=ft.Colors.WHITE),
                                    ], alignment=MainAxisAlignment.CENTER, ),

                                ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                            ]
                        ),
                        width=400,
                        height=500,
                    )
                ], alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Comedia", color=ft.Colors.WHITE, size=30,
                                                text_align=TextAlign.RIGHT),
                                        ft.Icon(ft.Icons.THEATER_COMEDY, color=ft.Colors.WHITE),
                                    ], alignment=MainAxisAlignment.CENTER, ),

                                ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                            ]
                        ),
                        width=400,
                        height=500,
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Romance", color=ft.Colors.WHITE, size=30,
                                                text_align=TextAlign.RIGHT),
                                        ft.Icon(ft.Icons.HEART_BROKEN, color=ft.Colors.WHITE),
                                    ], alignment=MainAxisAlignment.CENTER, ),

                                ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                            ]
                        ),
                        width=400,
                        height=500,
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Romance", color=ft.Colors.WHITE, size=30,
                                                text_align=TextAlign.RIGHT),
                                        ft.Icon(ft.Icons.HEART_BROKEN, color=ft.Colors.WHITE),
                                    ], alignment=MainAxisAlignment.CENTER, ),

                                ft.Image(src="imagenes/arania0.jpg", width=400, height=450, ),
                            ]
                        ),
                        width=400,
                        height=500,
                    )
                ], alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        ], scroll= ft.ScrollMode.ALWAYS,
        expand=True

    )
    page.add(categoria)
    page.update()


ft.app(target=main)