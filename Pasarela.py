import flet as ft
from flet.core.types import MainAxisAlignment


def Pasarela():
    imgPasarela = "imagenes/arania0.jpg"
    num = 0
    image_container = ft.Image(
        src=imgPasarela,
        fit=ft.ImageFit.COVER,
        height=500,
        width=600,
    )
    left_button = ft.IconButton(
        icon=ft.icons.CHEVRON_LEFT,
        icon_size=40,
        style=ft.ButtonStyle(color="white"),
    )

    right_button = ft.IconButton(
        icon=ft.icons.CHEVRON_RIGHT,
        icon_size=40,
        style=ft.ButtonStyle(color="white"),
    )
    imagenBotones = ft.Container(
        content=ft.Row(
            [
                left_button,

                ft.Column(
                    [
                        ft.Text(
                            "El Hombre Araña",
                            color="white",
                            size=50,
                            weight="bold",
                        ),
                        ft.Text(
                            "Científico, vigilante, profesor, fotógrafo, superhéroe. Fuerza, velocidad, durabilidad,"
                            " agilidad, sentidos, reflejos, coordinación, equilibrio y resistencia sobrehumanos. "
                            "Fisiología de la araña: Precognitiva capacidad de sentido arácnido, se aferra a la "
                            "mayoría de las superficies sólidas y la capacidad de las redes.",
                            color="white",
                            size=25,
                            width="bold"),
                        ft.ElevatedButton(width=150, content=ft.Text(value="Mas información.."))
                    ],
                    expand=True,
                ),
                image_container,
                right_button,
            ],
        ),
        height=500,
    )
    pasarela = ft.Column(
        controls=[
            ft.Text("Comedia",
                    size=50,
                    color="white"),
            ft.Row(
                controls=[
                    left_button,
                    ft.Container(content=ft.Image(src="imagenes/arania2.jpg", fit=ft.ImageFit.FILL
                                                  # Ajuste que permite distorsión
                                                  ), padding=4, width=164, height=200,),
                    ft.Container(content=ft.Image(src="imagenes/arania3.jpg", fit=ft.ImageFit.FILL
                                                  # Ajuste que permite distorsión
                                                  ), padding=4, width=164, height=200, ),
                    ft.Container(content=ft.Image(src="imagenes/arania2.jpg", fit=ft.ImageFit.FILL
                                                  # Ajuste que permite distorsión
                                                  ), padding=4, width=164, height=200, ),
                    ft.Container(content=ft.Image(src="imagenes/arania3.jpg", fit=ft.ImageFit.FILL
                                                  # Ajuste que permite distorsión
                                                  ), padding=4, width=164, height=200, ),
                    ft.Container(content=ft.Image(src="imagenes/arania3.jpg", fit=ft.ImageFit.FILL),
                                 padding=4, width=164, height=200),
                    ft.Container(content=ft.Image(src="imagenes/arania3.jpg", fit=ft.ImageFit.FILL
                                                  # Ajuste que permite distorsión
                                                  ), padding=4, width=164, height=200, ),
                    ft.Container(content=ft.Image(src="imagenes/arania3.jpg", fit=ft.ImageFit.FILL
                                                  # Ajuste que permite distorsión
                                                  ), padding=4, width=164, height=200, ),
                    right_button

                ],
                scroll=ft.ScrollMode.ALWAYS,

            )
        ]

    )
    scrollable = ft.Column(
        controls=[

            ft.Text("Inicio", color="white",size=50, text_align=ft.TextAlign.RIGHT,right=True ),

            imagenBotones,
            pasarela
        ],
        scroll=ft.ScrollMode.ALWAYS,  # Habilitar desplazamiento vertical
        expand=True,
    )
    return scrollable

