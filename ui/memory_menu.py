import tkinter as tk

# Define difficulty settings for the Memory Card Game.
MEMORY_DIFFICULTIES = {
    "Easy": {"rows": 4, "cols": 4, "time_limit": 120},
    "Medium": {"rows": 6, "cols": 6, "time_limit": 180},
    "Hard": {"rows": 8, "cols": 8, "time_limit": 240}
}

class MemorySettingsPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.selected_difficulty = tk.StringVar(value="Easy")
        self.create_widgets()

    def create_widgets(self):
        # Set grid layout with two uniform columns.
        self.grid_columnconfigure(0, weight=1, uniform="col")
        self.grid_columnconfigure(1, weight=1, uniform="col")
        self.grid_columnconfigure(2, weight=1, uniform="col")

        title = tk.Label(self, text="Memory Card Game Settings", font=("Arial", 20))
        title.grid(row=0, column=0, columnspan=3, pady=10)

        explanation = (
            "Select a difficulty level:\n"
            "Easy: 4x4 grid, 120 sec timer\n"
            "Medium: 6x6 grid, 180 sec timer\n"
            "Hard: 8x8 grid, 240 sec timer"
        )
        expl_label = tk.Label(self, text=explanation, font=("Arial", 10), justify="center")
        expl_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        row = 2
        for level in MEMORY_DIFFICULTIES.keys():
            rb = tk.Radiobutton(self, text=level, variable=self.selected_difficulty, value=level, font=("Arial", 12))
            rb.grid(row=row, column=0, columnspan=3, sticky="w", padx=10, pady=2)
            row += 1

        start_button = tk.Button(self, text="Start", font=("Arial", 14), width=12, command=self.start_game)
        start_button.grid(row=row, column=2, padx=10, pady=10, sticky="e")
        back_button = tk.Button(self, text="Back", font=("Arial", 14), width=12,
                                command=lambda: self.app.show_menu_page())
        back_button.grid(row=row, column=0, padx=10, pady=10, sticky="w")

    def start_game(self):
        difficulty = self.selected_difficulty.get()
        settings = MEMORY_DIFFICULTIES[difficulty]
        self.app.show_memory_game(settings)
