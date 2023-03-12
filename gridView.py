import os
import flet as ft
import random
import time

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    
    def change(e: ft.ControlEvent ):
        e.control.bgcolor=ft.colors.WHITE
        e.control.shape=ft.BoxShape.CIRCLE
        page.update()

    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    clrs = [ft.colors.RED, ft.colors.GREEN, ft.colors.BLUE]

    for i in range(30):
        ftt=ft.Text(f"Item {i}")

        gv.controls.append(
            ft.Container(
                ftt,
                alignment=ft.alignment.center,
                bgcolor= clrs[i%3],
                border=ft.border.all(1, ft.colors.BLUE),
                border_radius=ft.border_radius.all(5),
                on_click=change,
                ink=True
            )
        )

    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
#ft.app(target=main)