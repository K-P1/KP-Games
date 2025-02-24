import tkinter as tk

class TicTacToeModeSelectionPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        TicTacToeModeSelectionPage_L1 = tk.Label(self, text="Select Game Mode", font=("Arial", 36))
        TicTacToeModeSelectionPage_B1 = tk.Button(self, text="Multiplayer", command=self.start_multiplayer, width=20, height=5)
        TicTacToeModeSelectionPage_B2 = tk.Button(self, text="Single Player", command=self.start_single_player, width=20, height=5)
        TicTacToeModeSelectionPage_B3 = tk.Button(self, text="Back", command=self.back, width=20, height=5)

        TicTacToeModeSelectionPage_L1.grid(row=0, column=0, columnspan=3)
        TicTacToeModeSelectionPage_B1.grid(row=1, column=0)
        TicTacToeModeSelectionPage_B2.grid(row=1, column=1)
        TicTacToeModeSelectionPage_B3.grid(row=1, column=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def start_multiplayer(self):
        self.app.show_tictactoe_settings_page(multiplayer=True)

    def start_single_player(self):
        self.app.show_tictactoe_settings_page(multiplayer=False)

    def back(self):
        self.app.show_menu_page()


class TicTacToeSettingsPage(tk.Frame):
    def __init__(self, app, multiplayer):
        super().__init__(app.root)
        self.app = app
        self.multiplayer = multiplayer

        TicTacToeSettingsPage_L0 = tk.Label(self, text="Game Settings", font=("Arial", 36))
        TicTacToeSettingsPage_L0.grid(row=0, column=0, columnspan=2)

        if not self.multiplayer:
            TicTacToeSettingsPage_L1 = tk.Label(self, text="Select Difficulty:")
            self.difficulty_var = tk.StringVar(value="Easy")
            TicTacToeSettingsPage_R1 = tk.Radiobutton(self, text="Easy", variable=self.difficulty_var, value="Easy")
            TicTacToeSettingsPage_R2 = tk.Radiobutton(self, text="Medium", variable=self.difficulty_var, value="Medium")
            TicTacToeSettingsPage_R3 = tk.Radiobutton(self, text="Hard", variable=self.difficulty_var, value="Hard")
            TicTacToeSettingsPage_R4 = tk.Radiobutton(self, text="Expert (Beta)", variable=self.difficulty_var, value="Expert")

            TicTacToeSettingsPage_L1.grid(row=1, column=0, columnspan=2)
            TicTacToeSettingsPage_R1.grid(row=2, column=0, columnspan=2, sticky='w', padx=15)
            TicTacToeSettingsPage_R2.grid(row=3, column=0, columnspan=2, sticky='w', padx=15)
            TicTacToeSettingsPage_R3.grid(row=4, column=0, columnspan=2, sticky='w', padx=15)
            TicTacToeSettingsPage_R4.grid(row=5, column=0, columnspan=2, sticky='w', padx=15)
        else:
            self.difficulty_var = None

        TicTacToeSettingsPage_L2 = tk.Label(self, text="Who Goes First:")
        self.first_player_var = tk.StringVar(value="Player 1")
        TicTacToeSettingsPage_R5 = tk.Radiobutton(self, text="Player 1 (X)", variable=self.first_player_var, value="Player 1")
        TicTacToeSettingsPage_R6 = tk.Radiobutton(self, text="Player 2 (O)", variable=self.first_player_var, value="Player 2")
        TicTacToeSettingsPage_B1 = tk.Button(self, text="Start Game", command=self.start_game, width=15)
        TicTacToeSettingsPage_B2 = tk.Button(self, text="Back", command=self.back, width=15)

        TicTacToeSettingsPage_L2.grid(row=6, column=0, columnspan=2)
        TicTacToeSettingsPage_R5.grid(row=7, column=0, columnspan=2, sticky='w', padx=15)
        TicTacToeSettingsPage_R6.grid(row=8, column=0, columnspan=2, sticky='w', padx=15)
        TicTacToeSettingsPage_B1.grid(row=9, column=0)
        TicTacToeSettingsPage_B2.grid(row=9, column=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=2)

    def start_game(self):
        difficulty = self.difficulty_var.get() if self.difficulty_var else None
        first_player = self.first_player_var.get()
        self.app.show_tic_tac_toe_game(
            multiplayer=self.multiplayer,
            difficulty=difficulty,
            first_player=first_player
        )

    def back(self):
        self.app.show_tictactoe()
