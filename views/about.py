import flet as ft
from flet_route import Params,Basket
from .nav import bar_item

class About(ft.UserControl):
    def __init__(self):
        super().__init__()

    def view(self,page:ft.page,params:Params,basket:Basket):
        print(params)
        params.selected_index = 1
        print(basket)
        return ft.View(
            "/about",
            controls=[
                ft.Text("ABOUT"),
                bar_item(page, params.get("selected_index"))
            ]
        )