import flet as ft

def main(page: ft.Page):
    page.title = "Arrastrar y soltar imágenes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Lista de imágenes arrastrables
    imagenes = [
        "assets/meme1.jpg",
        "assets/meme2.jpg",
        "assets/meme3.jpg"
    ]

    # Imagen inicial por defecto para los huecos destino
    def imagen_inicial():
        return ft.Image(src="assets/meme1.jpg", width=100, height=100)

    # Función cuando se suelta una imagen
    def drag_accept(e: ft.DragTargetEvent):
        src_control = page.get_control(e.src_id)
        if src_control and hasattr(src_control, "content"):
            src_image_url = src_control.content.src
            e.control.content.content.src = src_image_url
            page.update()

    # Crear imágenes arrastrables
    draggable_images = [
        ft.Draggable(
            group="imagenes",
            content=ft.Image(src=img, width=100, height=100),
            content_feedback=ft.Image(src=img, width=70, height=70, opacity=0.7),
        )
        for img in imagenes
    ]

    # Crear varios contenedores destino (huecos)
    num_huecos = 3  # puedes cambiar este número según cuántos quieras
    drag_targets = [
        ft.DragTarget(
            group="imagenes",
            content=ft.Container(
                width=120,
                height=120,
                bgcolor=ft.Colors.BLUE_GREY_100,
                border_radius=20,
                alignment=ft.alignment.center,
                content=imagen_inicial(),
            ),
            on_accept=drag_accept,
        )
        for _ in range(num_huecos)
    ]

    # Mostrar todo en la página
    page.add(
        ft.Text("Arrastra una imagen y suéltala en cualquier recuadro", size=20),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            controls=draggable_images,
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            controls=drag_targets,
        ),
    )

ft.app(target=main, assets_dir=".")
