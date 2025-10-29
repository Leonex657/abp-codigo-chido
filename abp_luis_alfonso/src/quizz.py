import flet as ft

def main(page: ft.Page):
    page.title = "Quiz sobre la CPU"
    page.window_width = 950
    page.window_height = 800
    page.bgcolor = "#F0F4F8"
    page.padding = 30
    page.scroll = ft.ScrollMode.AUTO

    # -------------------- DATOS DEL QUIZ --------------------
    preguntas = [
        {
            "texto": "¿Cuál es la función principal de la ALU dentro de un microprocesador?",
            "imagen": "meme2.jpg",
            "opciones": [
                "a) Gestionar la memoria",
                "b) Ejecutar operaciones aritméticas y lógicas",
                "c) Coordinar los registros internos",
                "d) Controlar los dispositivos de entrada/salida"
            ],
            "correcta": 1
        },
        {
            "texto": "¿La ALU se encuentra contenida dentro de qué otro componente más general?",
            "imagen": "meme3.jpg",
            "opciones": ["a) GPU", "b) Unidad de Control", "c) Memoria RAM", "d) CPU"],
            "correcta": 3
        },
        {
            "texto": "¿Cuál es la responsabilidad principal de la Unidad de Control?",
            "imagen": "meme4.jpg",
            "opciones": [
                "a) Realizar cálculos aritméticos",
                "b) Almacenar datos temporalmente",
                "c) Coordinar la ejecución correcta de instrucciones",
                "d) Dibujar gráficos en pantalla"
            ],
            "correcta": 2
        },
        {
            "texto": "¿Qué otro componente siempre trabaja en conjunto con la Unidad de Control dentro de la CPU?",
            "imagen": "meme5.jpg",
            "opciones": ["a) Disco duro", "b) ALU", "c) ROM", "d) Tarjeta de red"],
            "correcta": 1
        },
        {
            "texto": "¿Qué tipo de información almacenan los registros?",
            "imagen": "meme6.jpg",
            "opciones": [
                "a) Información visual",
                "b) Información temporal durante la ejecución de instrucciones",
                "c) Configuraciones de hardware",
                "d) Datos almacenados permanentemente"
            ],
            "correcta": 1
        },
        {
            "texto": "¿Dónde se encuentran físicamente los registros?",
            "imagen": "meme7.jpg",
            "opciones": [
                "a) En la memoria RAM externa",
                "b) Dentro del disco duro",
                "c) Dentro de la CPU",
                "d) En la tarjeta gráfica"
            ],
            "correcta": 2
        },
        {
            "texto": "¿Qué muestra el diagrama completo presentado al final del programa?",
            "imagen": "meme8.jpg",
            "opciones": [
                "a) Cómo la GPU procesa imágenes",
                "b) Cómo los dispositivos de entrada y salida se conectan al CPU",
                "c) Cómo la CPU interactúa con memoria, entrada/salida y realiza procesamiento",
                "d) Cómo se programan videojuegos"
            ],
            "correcta": 2
        },
        {
            "texto": "¿Quién coordina todas las operaciones dentro del CPU según el diagrama?",
            "imagen": "meme9.jpg",
            "opciones": [
                "a) La memoria RAM",
                "b) Los registros",
                "c) La Unidad de Control",
                "d) El mouse y el teclado"
            ],
            "correcta": 2
        },
    ]

    # -------------------- COMPONENTES --------------------
    titulo = ft.Text("Quiz: Arquitectura de la CPU", size=34, weight="bold", color="#1F3C88")
    subtitulo = ft.Text("Responde correctamente para avanzar. Si fallas, deberás reiniciar.", size=18, color="#3E5060")
    imagen = ft.Image(src="meme1.jpg", width=450, height=280, fit=ft.ImageFit.CONTAIN)
    pregunta_texto = ft.Text("", size=24, weight="bold", color="#1F3C88", text_align=ft.TextAlign.CENTER)

    # Estado
    estado = {"indice": -1}

    # Botones de respuesta
    botones = []

    def crear_boton_respuesta(indice):
        b = ft.ElevatedButton(
            text="Botón",
            width=520,
            bgcolor="#4A90E2",
            color="white",
            visible=False,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=16),
                elevation=10,
                overlay_color="#6BB0F3"
            ),
        )

        def evento_click(e):
            idx = estado["indice"]
            correcta = preguntas[idx]["correcta"]
            if indice == correcta:
                siguiente = idx + 1
                if siguiente < len(preguntas):
                    mostrar_pregunta(siguiente)
                else:
                    mostrar_final_bueno()
            else:
                mostrar_final_malo()
        b.on_click = evento_click
        return b

    for i in range(4):
        botones.append(crear_boton_respuesta(i))

    btn_inicio = ft.ElevatedButton(
        text="¡Comenzar Quiz!",
        width=320,
        bgcolor="#43A047",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=16),
            elevation=12,
            overlay_color="#66BB6A"
        ),
    )

    btn_reiniciar = ft.ElevatedButton(
        text="Reiniciar",
        width=220,
        bgcolor="#D81B60",
        color="white",
        visible=False,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=16),
            elevation=10,
            overlay_color="#F06292"
        ),
    )

    # -------------------- FUNCIONES --------------------
    def mostrar_inicio():
        estado["indice"] = -1
        imagen.src = "meme1.jpg"
        pregunta_texto.value = ""
        for b in botones:
            b.visible = False
        btn_inicio.visible = True
        btn_reiniciar.visible = False
        page.update()

    def mostrar_pregunta(indice):
        estado["indice"] = indice
        q = preguntas[indice]
        imagen.src = q["imagen"]
        pregunta_texto.value = q["texto"]
        for i, b in enumerate(botones):
            b.text = q["opciones"][i]
            b.visible = True
        btn_inicio.visible = False
        btn_reiniciar.visible = False
        page.update()

    def mostrar_final_bueno():
        estado["indice"] = len(preguntas)
        imagen.src = "bueno.jpg"
        pregunta_texto.value = "🎉 ¡Felicidades! Has completado el quiz con éxito."
        for b in botones:
            b.visible = False
        btn_reiniciar.visible = True
        page.update()

    def mostrar_final_malo():
        estado["indice"] = -99
        imagen.src = "malo.jpg"
        pregunta_texto.value = "❌ Has fallado el quiz. Reinicia para intentarlo nuevamente."
        for b in botones:
            b.visible = False
        btn_reiniciar.visible = True
        page.update()

    def iniciar_quiz(e):
        mostrar_pregunta(0)

    def reiniciar_quiz(e):
        mostrar_inicio()

    btn_inicio.on_click = iniciar_quiz
    btn_reiniciar.on_click = reiniciar_quiz

    # -------------------- LAYOUT --------------------
    card = ft.Container(
        content=ft.Column(
            [
                titulo,
                subtitulo,
                imagen,
                pregunta_texto,
                ft.Column(botones, alignment=ft.MainAxisAlignment.CENTER, spacing=12),
                ft.Row([btn_inicio, btn_reiniciar], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=25,
        ),
        alignment=ft.alignment.center,
        bgcolor="white",
        border_radius=20,
        padding=30,
        shadow=ft.BoxShadow(blur_radius=22, color="#B0BEC5", offset=ft.Offset(6, 6)),
        width=780,
    )

    page.add(ft.Row([card], alignment=ft.MainAxisAlignment.CENTER))
    mostrar_inicio()

ft.app(target=main)