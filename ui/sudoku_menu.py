import tkinter as tk
from tkinter import messagebox

class SudokuSettingsPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        SudokuSettingsPage_L1 = tk.Label(self, text="Select Difficulty Level:", font=("Arial", 36))
        self.difficulty_var = tk.StringVar(value="easy")
        SudokuSettingsPage_R1 = tk.Radiobutton(self, text="Easy", variable=self.difficulty_var, value="easy", command=self.show_difficulty_info)
        SudokuSettingsPage_R2 = tk.Radiobutton(self, text="Medium", variable=self.difficulty_var, value="medium", command=self.show_difficulty_info)
        SudokuSettingsPage_R3 = tk.Radiobutton(self, text="Hard", variable=self.difficulty_var, value="hard", command=self.show_difficulty_info)
        SudokuSettingsPage_R4 = tk.Radiobutton(self, text="Expert", variable=self.difficulty_var, value="expert", command=self.show_difficulty_info)
        SudokuSettingsPage_B1 = tk.Button(self, text="Start Game", command=self.start_game, width=15)
        SudokuSettingsPage_B2 = tk.Button(self, text="Back", command=self.back, width=15)

        self.info_label = tk.Label(self, text="", height=2, font=("Arial", 16))

        SudokuSettingsPage_L1.grid(row=0, column=0, columnspan=2, sticky='we')
        SudokuSettingsPage_R1.grid(row=1, column=0, sticky='w', padx=15)
        SudokuSettingsPage_R2.grid(row=2, column=0, sticky='w', padx=15)
        SudokuSettingsPage_R3.grid(row=3, column=0, sticky='w', padx=15)
        SudokuSettingsPage_R4.grid(row=4, column=0, sticky='w', padx=15)
        SudokuSettingsPage_B2.grid(row=5, column=0, sticky='w', padx=15)
        SudokuSettingsPage_B1.grid(row=5, column=1, sticky='e', padx=15)
        self.info_label.grid(row=6, column=0, columnspan=2, sticky='we')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=2)

        self.show_difficulty_info()

    def show_difficulty_info(self):
        difficulty = self.difficulty_var.get()
        info = {
            "easy": "Easy level with more given numbers.",
            "medium": "Medium level with a balanced number of given numbers.",
            "hard": "Hard level with fewer given numbers.",
            "expert": "Expert level with very few given numbers."
        }
        self.info_label.config(text=info[difficulty])

    def start_game(self):
        difficulty = self.difficulty_var.get()
        self.app.show_sudoku_game(difficulty)

    def back(self):
        self.app.show_menu_page()
