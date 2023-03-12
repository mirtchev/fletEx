import os
import flet as ft
import random
import time

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    clrs = [ft.colors.RED, ft.colors.GREEN, ft.colors.BLUE]

    for i in range(3):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor= clrs[i%3],
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )

    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
#ft.app(target=main)