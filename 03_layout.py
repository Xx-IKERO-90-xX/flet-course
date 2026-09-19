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
        ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=True,
                            alignment=ft.Alignment.CENTER,
                            bgcolor=ft.Colors.RED,
                            content=ft.Text("Etiqueta 1", color='black')
                        ),
                        ft.Container(
                            #expand=True,
                            alignment=ft.Alignment.CENTER,
                            bgcolor=ft.Colors.RED,
                            content=ft.Text("Etiqueta 3", color='black')
                        )
                    ]
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.AMBER,
                    content=ft.Text("Etiqueta 1", color='black')
                ),
                ft.Container(
                    #expand=True,
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.AMBER,
                    content=ft.Text("Etiqueta 3", color='black')
                )
            ]
        )
    )

ft.run(main)