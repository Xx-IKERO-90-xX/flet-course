import flet as ft
from view.home_view import HomeView

def main(page: ft.Page):
    page.title = "PanaGaming Launcher"
    page.window.width = 950
    page.window.height = 600
    page.window.resizable = False
    page.bgcolor = "#0f172a"  # Fondo oscuro cyberpunk

    # Menú superior estilo pestañas (Sin iconos)
    top_nav = ft.Row(
        spacing=10,
        controls=[
            ft.TextButton("Inicio", style=ft.ButtonStyle(color=ft.Colors.WHITE)),
            ft.TextButton("Instancias", style=ft.ButtonStyle(color=ft.Colors.WHITE70)),
            ft.TextButton("Mods / Packs", style=ft.ButtonStyle(color=ft.Colors.WHITE70)),
            ft.TextButton("Ajustes", style=ft.ButtonStyle(color=ft.Colors.WHITE70)),
        ]
    )
    
    content_area = ft.Container(expand=True, content=HomeView(page))

    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    bgcolor="#1e293b",
                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                    content=top_nav
                ),
                ft.Divider(height=1, color="#334155"),
                content_area
            ]
        )
    )

ft.app(target=main)