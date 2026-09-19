import flet as ft

def main(page: ft.Page):
    page.title = "Estilos"

    page.window.height = 500
    page.window.width = 1000
    
    page.window.resizable = False
    #page.pgcolor = "white"

    page.theme_mode = "light"
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.GREEN_50,
        font_family='Comic Sans Ms'
    )
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    page.add(
        ft.Text("Ejemplo", color='black')
    )

ft.run(main)