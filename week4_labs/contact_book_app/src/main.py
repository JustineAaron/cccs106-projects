import flet as ft
from database import init_db
from app_logic import display_contacts, add_contact

def main(page: ft.Page):
    page.title = "Contact Book"
    page.window_width = 400
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Colors
    LIGHT_MINT = "#DFFCF2"
    DARK_MINT = "#2E8B57"
    page.bgcolor = LIGHT_MINT

    db_conn = init_db()

    # Input fields
    name_input = ft.TextField(label="Name", width=350)
    phone_input = ft.TextField(label="Phone", width=350)
    email_input = ft.TextField(label="Email", width=350)

    contacts_list_view = ft.ListView(expand=1, spacing=10, auto_scroll=True)

    # Aesthetic Log In button
    login_button = ft.ElevatedButton(
        text="Log In",
        width=220,
        height=50,
        style=ft.ButtonStyle(
            bgcolor="#2E8B57",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=25),
            elevation=5,
        ),
        on_click=lambda e: add_contact(
            page, (name_input, phone_input, email_input), contacts_list_view, db_conn
        ),
    )

    # Dark mode state
    dark_mode = {"enabled": False}

    # Toggle dark mode
    def toggle_theme(e):
        if dark_mode["enabled"]:
            page.bgcolor = LIGHT_MINT
            theme_button.text = "🌙 Dark Mode"
            login_button.style.bgcolor = "#2E8B57"
            dark_mode["enabled"] = False
        else:
            page.bgcolor = DARK_MINT
            theme_button.text = "☀️ Light Mode"
            login_button.style.bgcolor = "#145a43"
            dark_mode["enabled"] = True
        page.update()

    # Dark mode button
    theme_button = ft.ElevatedButton(
        text="🌙 Dark Mode",
        on_click=toggle_theme,
        style=ft.ButtonStyle(
            bgcolor="#0b5f4b",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=20),
        ),
    )

    # Layout
    page.add(
        ft.Column(
            [
                ft.Row([theme_button], alignment=ft.MainAxisAlignment.END),  # top right
                ft.Text("Enter Contact Details:", size=20, weight=ft.FontWeight.BOLD),
                name_input,
                phone_input,
                email_input,
                ft.Row([login_button], alignment=ft.MainAxisAlignment.CENTER),  # centered login
                ft.Divider(),
                ft.Text("Contacts:", size=20, weight=ft.FontWeight.BOLD),
                contacts_list_view,
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

    display_contacts(page, contacts_list_view, db_conn)


if __name__ == "__main__":
    ft.app(target=main)
