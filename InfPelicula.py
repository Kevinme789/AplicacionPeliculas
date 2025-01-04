import flet as ft
from flet.core.types import MainAxisAlignment

import AppBar

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.appbar = AppBar.Appbar()
    page.update()
    info = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text("Hombre Araña",size=50,color=ft.Colors.WHITE),
                ],alignment=MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Image(src="imagenes/arania0.jpg",width=400,height=450),
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Científico, vigilante, profesor, fotógrafo, superhéroe. Fuerza, velocidad, durabilidad,"
                                " agilidad, sentidos, reflejos, coordinación, equilibrio y resistencia sobrehumanos. "
                                "Fisiología de la araña: Precognitiva capacidad de sentido arácnido, se aferra a la "
                                "mayoría de las superficies sólidas y la capacidad de las redes.",
                                color="white",
                                size=25),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.DATE_RANGE, size=25, color=ft.Colors.BLUE_GREY),
                                    ft.Text("Fecha de Estreno: ", size=25, color=ft.Colors.BLUE_GREY),
                                    ft.Text("1998-03-05",size=23, color=ft.Colors.BLUE_GREY),
                                ],
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.PERSON,size=25, color=ft.Colors.BLUE_GREY),
                                    ft.Text("Rating: ", size=25, color=ft.Colors.BLUE_GREY),
                                    ft.Text("2.3",size=23,color=ft.Colors.BLUE_GREY),
                                    ft.Icon(ft.Icons.STAR,size=25,color=ft.Colors.BLUE_GREY),
                                ],
                            ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.LANGUAGE, size=25, color=ft.Colors.BLUE_GREY),
                                ft.Text("Idiomas: ", size=25, color=ft.Colors.BLUE_GREY),
                                ft.Text("Español, Ingles", size=23, color=ft.Colors.BLUE_GREY),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.RECENT_ACTORS, size=25, color=ft.Colors.BLUE_GREY),
                                ft.Text("Director: ", size=25, color=ft.Colors.BLUE_GREY),
                                ft.Text("GuyRitchie", size=23, color=ft.Colors.BLUE_GREY),
                            ]
                        ),
                        ],expand=True,width=400,height=450
                    )
                ],alignment=MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Column(
                controls=[
                    ft.Text("Cast",size=50,color=ft.Colors.WHITE),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(image_src="imagenes/actor0.jpg",width=150,height=150,
                                         shape=ft.BoxShape.CIRCLE,image_fit=ft.ImageFit.COVER),
                                    ft.Text("Dwayne Johnson",size=20,color=ft.Colors.WHITE),
                                    ft.Text("Director",size=20,color=ft.Colors.BLUE_GREY,),
                                         ],
                            ),
                            ft.Column(
                                controls=[
                                    ft.Container(image_src="imagenes/actor0.jpg", width=150, height=150,
                                                 shape=ft.BoxShape.CIRCLE, image_fit=ft.ImageFit.COVER),
                                    ft.Text("Dwayne Johnson", size=20, color=ft.Colors.WHITE),
                                    ft.Text("Actor", size=20, color=ft.Colors.BLUE_GREY, ),
                                ],
                            ),

                        ]
                    )
                ]
            ),
            ft.Column(
                controls=[
                    ft.Text("Crew", size=50, color=ft.Colors.WHITE),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(image_src="imagenes/actor0.jpg", width=150, height=150,
                                                 shape=ft.BoxShape.CIRCLE, image_fit=ft.ImageFit.COVER),
                                    ft.Text("Dwayne Johnson", size=20, color=ft.Colors.WHITE),
                                    ft.Text("Productor", size=20, color=ft.Colors.BLUE_GREY, ),
                                ],
                            ),
                            ft.Column(
                                controls=[
                                    ft.Container(image_src="imagenes/actor0.jpg", width=150, height=150,
                                                 shape=ft.BoxShape.CIRCLE, image_fit=ft.ImageFit.COVER),
                                    ft.Text("Dwayne Johnson", size=20, color=ft.Colors.WHITE),
                                    ft.Text("Guionista", size=20, color=ft.Colors.BLUE_GREY, ),
                                ],
                            ),

                        ]
                    )
                ]
            )
        ],scroll=ft.ScrollMode.ALWAYS,
        expand=True

    )

    page.add(info)

ft.app(target=main)


