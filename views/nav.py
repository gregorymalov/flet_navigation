import flet as ft

def bar_item(page, selected_index):
    def change_page(e):
        page.update()
        if e.control.selected_index == 0:
            page.go("/")
            page.update()
        if e.control.selected_index == 1:
            page.go("/about")
            page.update()
        if e.control.selected_index == 2:
            page.go("/wallet")
            page.update()

    page.update()

    page.navigation_bar = ft.NavigationBar(
        bgcolor="blue",
        on_change=lambda e: change_page(e),
        selected_index = selected_index,
        destinations = [
        ft.NavigationDestination(icon="FINGERPRINT_OUTLINED", label="Home"),
        ft.NavigationDestination(icon="PEOPLE_OUTLINE", label="About"),
        ft.NavigationDestination(icon="ACCOUNT_BALANCE_WALLET_OUTLINED", label="Wallet"),
        ]
        )
    
    return page.navigation_bar



