import tkinter as tk

# Map difficulty levels to Snake game settings.
SNAKE_DIFFICULTIES = {
    "Easy":    {"speed": 5,  "wrap": True,  "food_multiplier": 2},
    "Medium":  {"speed": 7,  "wrap": True,  "food_multiplier": 1.5},
    "Hard":    {"speed": 10, "wrap": True,  "food_multiplier": 1},
    "Expert":  {"speed": 15, "wrap": False, "food_multiplier": 1}
}

class SnakeSettingsPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.selected_difficulty = tk.StringVar(value="Medium")
        self.create_widgets()

    def create_widgets(self):
        # Configure grid with two uniform columns.
        self.grid_columnconfigure(0, weight=1, uniform="col")
        self.grid_columnconfigure(1, weight=1, uniform="col")
        self.grid_columnconfigure(2, weight=1, uniform="col")

        title = tk.Label(self, text="Snake Game Settings", font=("Arial", 20))
        title.grid(row=0, column=0, columnspan=3, pady=10)

        explanation = (
            "Select a difficulty level:\n"
            "Easy: Slow speed, wrap enabled, more food\n"
            "Medium: Moderate speed, wrap enabled\n"
            "Hard: Fast speed, wrap enabled\n"
            "Expert: Very fast speed, no wrap"
        )
        explanation_label = tk.Label(self, text=explanation, font=("Arial", 10), justify="center")
        explanation_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        row = 2
        for level in SNAKE_DIFFICULTIES.keys():
            rb = tk.Radiobutton(self, text=level, variable=self.selected_difficulty, value=level, font=("Arial", 12))
            rb.grid(row=row, column=0, columnspan=2, sticky="w", padx=10, pady=2)
            row += 1

        start_button = tk.Button(self, text="Start Snake", font=("Arial", 12), width=12, command=self.start_game)
        start_button.grid(row=row, column=2, padx=10, pady=10, sticky="e")

        back_button = tk.Button(self, text="Back", font=("Arial", 12), width=12,
                                command=lambda: self.app.show_menu_page())
        back_button.grid(row=row, column=0, padx=10, pady=10, sticky="w")

    def start_game(self):
        difficulty = self.selected_difficulty.get()
        settings = SNAKE_DIFFICULTIES[difficulty]
        self.app.show_snake_game(settings)
