import tkinter as tk

# Define difficulty settings.
MINESWEEPER_DIFFICULTIES = {
    "Easy": {"rows": 9, "cols": 9, "mines": 10},
    "Medium": {"rows": 16, "cols": 16, "mines": 40},
    "Hard": {"rows": 16, "cols": 30, "mines": 99}
}

class MinesweeperSettingsPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.selected_difficulty = tk.StringVar(value="Easy")
        self.create_widgets()

    def create_widgets(self):
        # Use grid layout with two uniform columns.
        self.grid_columnconfigure(0, weight=1, uniform="col")
        self.grid_columnconfigure(1, weight=1, uniform="col")
        self.grid_columnconfigure(2, weight=1, uniform="col")
        
        title = tk.Label(self, text="Minesweeper Settings", font=("Arial", 20))
        title.grid(row=0, column=0, columnspan=3, pady=10)
        
        explanation = ("Select difficulty level:\n"
                       "Easy: 9x9 grid, 10 mines\n"
                       "Medium: 16x16 grid, 40 mines\n"
                       "Hard: 16x30 grid, 99 mines")
        expl_label = tk.Label(self, text=explanation, font=("Arial", 10), justify="center")
        expl_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
        
        row = 2
        for level in MINESWEEPER_DIFFICULTIES.keys():
            rb = tk.Radiobutton(self, text=level, variable=self.selected_difficulty, value=level, font=("Arial", 12))
            rb.grid(row=row, column=0, columnspan=3, sticky="w", padx=10, pady=2)
            row += 1
        
        start_button = tk.Button(self, text="Start", font=("Arial", 12), width=12, command=self.start_game)
        start_button.grid(row=row, column=2, padx=10, pady=10, sticky="e")
        back_button = tk.Button(self, text="Back", font=("Arial", 12), width=12,
                                command=lambda: self.app.show_menu_page())
        back_button.grid(row=row, column=0, padx=10, pady=10, sticky="w")

    def start_game(self):
        difficulty = self.selected_difficulty.get()
        settings = MINESWEEPER_DIFFICULTIES[difficulty]
        self.app.show_minesweeper_game(settings)
