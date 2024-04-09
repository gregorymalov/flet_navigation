import flet as ft
from flet_route import Params,Basket
from .nav import bar_item

class Wallet(ft.UserControl):
    def __init__(self):
        super().__init__()

    def view(self,page:ft.page,params:Params,basket:Basket):
        print(params)
        print(basket)
        params.selected_index = 2
        return ft.View(
            "/wallet",
            controls=[
                ft.Text("WALLET"),
                bar_item(page, params.get("selected_index"))
            ]
        )