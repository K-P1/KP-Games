import tkinter as tk
from tkinter import messagebox
from games.hangman import DIFFICULTY_SETTINGS

class HangmanSettingsPage(tk.Frame):
    """
    Settings page for Hangman.
    Players select a difficulty level which determines the number of turns and hints.
    """
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.selected_difficulty = tk.StringVar(value="Easy")
        self.grid_columnconfigure(0, weight=1, uniform="col")
        self.grid_columnconfigure(1, weight=1, uniform="col")
        self.grid_columnconfigure(2, weight=1, uniform="col")
        self.create_widgets()


    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Hangman Settings", font=("Arial", 20), justify="center")
        title.grid(row=0, column=0, columnspan=3, pady=12)

        # Explanation
        explanation = (
            "Select a difficulty level:\n\n"
            "Easy: 10 attempts and 3 hints\n"
            "Medium: 8 attempts and 2 hints\n"
            "Hard: 6 attempts and 1 hint\n"
            "Expert: 6 attempts and 0 hints"
        )
        explanation_label = tk.Label(self, text=explanation, font=("Arial", 10), justify="center")
        explanation_label.grid(row=1, column=0, columnspan=3, padx=10, pady=8)

        # Radio buttons for difficulty selection.
        row = 2
        for level in DIFFICULTY_SETTINGS.keys():
            rb = tk.Radiobutton(self, text=level, variable=self.selected_difficulty, value=level, font=("Arial", 12))
            rb.grid(row=row, column=0, columnspan=3, sticky="w", padx=10, pady=2)
            row += 1

        # Back and Start buttons.
        back_button = tk.Button(self, text="Back", font=("Arial", 12), width=10,
                                command=lambda: self.app.show_menu_page())
        back_button.grid(row=row, column=0, padx=10, pady=10, sticky="w")

        start_button = tk.Button(self, text="Start", font=("Arial", 12), width=10,
                                 command=self.start_game)
        start_button.grid(row=row, column=2, padx=10, pady=10, sticky="e")

    def start_game(self):
        difficulty = self.selected_difficulty.get()
        settings = DIFFICULTY_SETTINGS[difficulty]
        self.app.show_hangman_game(settings)
