import flet as ft
import mysql.connector
from db_connection import connect_db

def main(page: ft.Page):
    page.title = "User Login"
    page.window_width = 400
    page.window_height = 350
    page.window_frameless = True
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#FFBF00"  # amber background

    # --- Input fields ---
    username = ft.TextField(
        label="User name",
        hint_text="Enter your user name",
        width=300,
    )

    password = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        password=True,
        can_reveal_password=True,
        width=300,
    )

    # --- Login button ---
    login_button = ft.ElevatedButton(text="Login", width=150)

    # --- Login handler ---
    def login_click(e):
        uname = username.value.strip()
        pwd = password.value.strip()

        if not uname or not pwd:
            dlg = ft.AlertDialog(title=ft.Text("Input Error"), content=ft.Text("Please enter username and password"))
            page.dialog = dlg
            dlg.open = True
            page.update()
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (uname, pwd))
            row = cursor.fetchone()
            cursor.close()
            conn.close()

            if row:
                dlg = ft.AlertDialog(title=ft.Text("Login Successful"), content=ft.Text(f"Welcome, {uname}!"))
            else:
                dlg = ft.AlertDialog(title=ft.Text("Login Failed"), content=ft.Text("Invalid username or password"))
        except mysql.connector.Error:
            dlg = ft.AlertDialog(title=ft.Text("Database Error"), content=ft.Text("An error occurred while connecting to the database"))

        page.dialog = dlg
        dlg.open = True
        page.update()

    login_button.on_click = login_click

    # --- Layout ---
    page.add(
        ft.Column(
            [
                ft.Text("User Login", size=20, weight="bold"),
                username,
                password,
                ft.Row([login_button], alignment="center"),  # ✅ Centered button
            ],
            spacing=20,
            alignment="center",
            horizontal_alignment="center",
        )
    )

ft.app(target=main)
