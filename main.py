import flet as ft
from flet_route import Routing,path
from views.home import Home # Here IndexView is imported from views/index_view.py
from views.about import About # Here NextView is imported from views/next_view.py
from views.wallet import Wallet 

def main(page: ft.Page):
    theme = ft.Theme()
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme
    page.update()
    
    app_routes = [
        path(
            url="/", # Here you have to give that url which will call your view on mach
            clear=False, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=Home().view # Here you have to pass a function or method which will take page,params and basket and return ft.View (If you are using class based view then you have to pass method name like IndexView().view .)
            ),
        path(
            url="/about", # Here you have to give that url which will call your view on mach
            clear=False, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=About().view # Here you have to pass a function or method which will take page,params and basket and return ft.View (If you are using class based view then you have to pass method name like IndexView().view .)
            ),
        path(
            url="/wallet", # Here you have to give that url which will call your view on mach
            clear=False, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=Wallet().view # Here you have to pass a function or method which will take page,params and basket and return ft.View (If you are using class based view then you have to pass method name like IndexView().view .)
            ),
        # path(url="/next_view/:my_id", clear=False, view=NextView().view),
    ]

    Routing(
        page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
        )
    page.go(page.route)

ft.app(target=main)