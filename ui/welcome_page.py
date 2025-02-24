import tkinter as tk
from tkinter import messagebox

class WelcomePage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        WelcomePage_L1 = tk.Label(self, text="Welcome to KP-Games", font=("Arial", 36))
        WelcomePage_B1 = tk.Button(self, text="Login", command=self.login, width=25, height=3)
        WelcomePage_B2 = tk.Button(self, text="Sign Up", command=self.sign_up, width=25, height=3)
        WelcomePage_B3 = tk.Button(self, text="Proceed as Guest", command=self.proceed_as_guest, width=25, height=3)
        WelcomePage_B4 = tk.Button(self, text="Exit", command=self.quit, width=25, height=3)

        WelcomePage_L1.grid(row=0, column=0, columnspan=2)
        WelcomePage_B1.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        WelcomePage_B2.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
        WelcomePage_B3.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        WelcomePage_B4.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def login(self):
        messagebox.showinfo("Login", "Login feature coming soon!")

    def sign_up(self):
        messagebox.showinfo("Sign Up", "Sign-up feature coming soon!")

    def proceed_as_guest(self):
        self.app.show_menu_page()

    def quit(self) -> None:
        return super().quit()
