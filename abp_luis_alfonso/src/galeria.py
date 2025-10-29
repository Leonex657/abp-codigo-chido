import flet as ft
import flet_video as fv

def main(page: ft.Page):
    page.title = "Anime"
    page.bgcolor = "#7E8FF3BA"

    videos = [
        {
            "titulo": "John Von Neumann",
            "descripcion": "Yo propuse la arquitectura de von Neumann, el modelo de diseño para computadoras que almacenan instrucciones y datos en la misma memoria",
            "videos": "https://github.com/ximSg1410/PIONEROS/raw/refs/heads/main/John_Von_Neuman_Matematico_Polimata_y_Sus_Contribuciones_Multidisciplinarias__10-22%2017_48.mp4",
        },
        {
            "titulo": "Unidad Aritmético Lógica",
            "descripcion": "Explicación sobre el diseño de la ALU y su función.",
            "videos": "https://github.com/ximSg1410/PIONEROS/raw/refs/heads/main/Unidad_Aritmetico_Logica_Funcion_y_Diseno_en_Computadoras_Digitales__10-22%2018_30.mp4",
        },
        {
            "titulo": "Unidad de Control",
            "descripcion": "Descripción de la Unidad de Control y su importancia en la CPU.",
            "videos": "https://github.com/ximSg1410/PIONEROS/raw/refs/heads/main/La_Unidad_de_Control_La_Mente_de_la_Maquina__10-22%2018_16.mp4",
        },
        {
            "titulo": "Registros",
            "descripcion": "Función y ubicación de los registros dentro de la CPU.",
            "videos": "https://github.com/ximSg1410/PIONEROS/raw/refs/heads/main/Funcionamiento_y_Uso_de_los_Registros_en_la_Memoria_de_la_Maquina__10-22%2018_29.mp4",
        },
        {
            "titulo": "Diagrama Completo de la CPU",
            "descripcion": "Análisis del diagrama completo de la CPU y sus componentes.",
            "videos": "https://github.com/Leonex657/Jonh-von/raw/refs/heads/main/WhatsApp%20Video%202025-10-22%20at%209.18.12%20PM.mp4",
        }
    ]

    componentes = [
        {
            "titulo": "ALU",
            "funcion": "La Unidad de Aritmética/Lógica realiza operaciones aritméticas y lógicas dentro del microprocesador.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/alu.jpg",
        },
        {
            "titulo": "Control",
            "funcion": "La Unidad de Control gestiona las operaciones dentro de la CPU para que las instrucciones se ejecuten correctamente.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/control.JPG",
        },
        {
            "titulo": "Registros",
            "funcion": "Los registros son unidades de almacenamiento temporal dentro de la CPU.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/registros.JPG",
        },
        {
            "titulo": "Diagrama Completo",
            "funcion": "Muestra cómo la CPU recibe datos, los procesa y devuelve resultados, todo coordinado por la unidad de control.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/completo.jpg",
        }
    ]

    indice_actual = [0]

    contenedor_contenido = ft.Container(expand=True)

    boton_siguiente = ft.ElevatedButton(text="Siguiente", bgcolor=ft.Colors.BLUE_400, color=ft.Colors.WHITE)
    boton_anterior = ft.ElevatedButton(text="Anterior", bgcolor=ft.Colors.GREY_600, color=ft.Colors.WHITE)

    # --- Función para mostrar el contenido ---
    def mostrar_contenido():
        contenedor_contenido.content = None

        if indice_actual[0] == 0:
            # 🟢 Primer video: solo presentación
            vid = videos[0]
            contenedor_contenido.content = ft.Column(
                [
                    fv.Video(
                        expand=True,
                        playlist=[fv.VideoMedia(vid["videos"])],
                        width=700,
                        height=800,
                        autoplay=True,
                        show_controls=True,
                    ),
                    ft.Text(vid["titulo"], size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(vid["descripcion"], size=16, color=ft.Colors.WHITE70, italic=True),
                    ft.Row([boton_siguiente], alignment=ft.MainAxisAlignment.CENTER),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            )

        else:
            # 🟡 Vista combinada (video + componente)
            vid = videos[indice_actual[0]]  # segundo video
            comp = componentes[(indice_actual[0] - 1) % len(componentes)]

            video_col = ft.Container(
                content=fv.Video(
                    playlist=[fv.VideoMedia(vid["videos"])],
                    width=500,
                    height=600,
                    autoplay=True,
                    show_controls=True,
                ),
                alignment=ft.alignment.center,
            )

            componente_col = ft.Column(
                [
                    ft.Image(src=comp["imagen"], width=400, height=350, fit=ft.ImageFit.CONTAIN),
                    ft.Text(comp["titulo"], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200),
                    ft.Text(comp["funcion"], size=14, color=ft.Colors.WHITE70, text_align=ft.TextAlign.JUSTIFY),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )

            contenedor_contenido.content = ft.Column(
                [
                    ft.Row(
                        [video_col, componente_col],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40,
                    ),
                    ft.Row(
                        [boton_anterior, boton_siguiente],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=50,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=25,
            )

        page.update()

    # --- Funciones de botones ---
    def siguiente_click(e):
        if indice_actual[0] < len(componentes):
            indice_actual[0] += 1
        mostrar_contenido()

    def anterior_click(e):
        if indice_actual[0] > 0:
            indice_actual[0] -= 1
        mostrar_contenido()

    boton_siguiente.on_click = siguiente_click
    boton_anterior.on_click = anterior_click

    # --- Layout principal ---
    page.add(
        ft.Container(
            content=contenedor_contenido,
            alignment=ft.alignment.center,
            expand=True,
            padding=20,
        )
    )

    mostrar_contenido()

ft.app(main)
