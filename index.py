import flet as ft

def main(page: ft.Page):
    page.title = "Prueba"
    
    page.window.height = 500
    page.window.width = 500
    
    page.window.resizable = False
    page.pgcolor = "white"
    
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    page.add(
        ft.Container(
            width=200,
            height=200,
            margin=50,
            padding=10,
            border_radius=5,
            alignment=ft.Alignment.BOTTOM_RIGHT,
            bgcolor=ft.Colors.AMBER,
            content=ft.Text("Etiqueta 1", color="black")
        )
    )

ft.run(main)