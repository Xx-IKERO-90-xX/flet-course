import flet as ft

def main(page: ft.Page):
    #------------ Configuración Ventana -------------
    page.title = "Etiquetas"

    page.window.height = 500
    page.window.width = 500
    
    page.window.resizable = False
    page.pgcolor = "white"
    
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    page.theme_mode = "light"
    page.theme = ft.Theme(
        color_scheme_seed = "cyan"
    )

    ts = ft.TextStyle(
        color=ft.Colors.BLACK,
        size=24,
        font_family='Times New Roman',
        bgcolor='red',
        italic=False,
        weight=ft.FontWeight.BOLD,
    )

    page.add(
        ft.Text("Hola Mundo", style=ts),
        ft.Text("Hola Mundo", style=ts)
    )

ft.run(main)