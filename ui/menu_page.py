import tkinter as tk

class MenuPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        
        MenuPage_L1 = tk.Label(self, text="Select a Game", font=("Arial", 36))
        MenuPage_B1 = tk.Button(self, text="Tic-Tac-Toe", command=self.start_tictactoe, width=20, height=6)
        MenuPage_B2 = tk.Button(self, text="Sudoku", command=self.start_sudoku, width=20, height=6)
        MenuPage_B3 = tk.Button(self, text="Number Guessing", command=self.start_number_guessing, width=20, height=6)
        MenuPage_B4 = tk.Button(self, text="Hangman", command=self.start_hangman, width=20, height=6)
        MenuPage_B5 = tk.Button(self, text="Rock, Paper, Scissors", command=self.start_rock_paper_scissors, width=20, height=6)
        MenuPage_B6 = tk.Button(self, text="Snake", command=self.start_snake, width=20, height=6)
        MenuPage_B7 = tk.Button(self, text="Minesweeper", command=self.start_minesweeper, width=20, height=6)
        MenuPage_B8 = tk.Button(self, text="Memory", command=self.start_memory, width=20, height=6)
        MenuPage_B9 = tk.Button(self, text="Quit", command=self.app.show_welcome_page, width=20, height=6)


        MenuPage_L1.grid(row=0, column=0, columnspan=3)
        MenuPage_B1.grid(row=1, column=0, pady=5)
        MenuPage_B2.grid(row=1, column=1, pady=5)
        MenuPage_B3.grid(row=1, column=2, pady=5)
        MenuPage_B4.grid(row=2, column=0, pady=5)
        MenuPage_B5.grid(row=2, column=1, pady=5)
        MenuPage_B6.grid(row=2, column=2, pady=5)
        MenuPage_B7.grid(row=3, column=0, pady=5)
        MenuPage_B8.grid(row=3, column=1, pady=5)
        MenuPage_B9.grid(row=3, column=2, pady=5)


        for i in range(3):
            self.grid_columnconfigure(i, weight=1, uniform="columns")
        self.grid_rowconfigure(0, weight=1, uniform="rows")
        for i in range(4):
            self.grid_rowconfigure(i, weight=2, uniform="rows")

    def start_tictactoe(self):
        self.app.show_tictactoe()

    def start_sudoku(self):
        self.app.show_sudoku_settings_page()

    def start_number_guessing(self):
        self.app.show_number_guessing_game()

    def start_hangman(self):
        self.app.show_hangman_settings()

    def start_rock_paper_scissors(self):
        self.app.show_rock_paper_scissors()

    def start_snake(self):
        self.app.show_snake_settings()

    def start_minesweeper(self):
        self.app.show_minesweeper_settings()

    def start_memory(self):
        self.app.show_memory_settings()
