import tkinter as tk
from ui.welcome_page import WelcomePage
from ui.menu_page import MenuPage
from ui.tictactoe_menu import TicTacToeModeSelectionPage, TicTacToeSettingsPage
from ui.sudoku_menu import SudokuSettingsPage
from games.tictactoe import TicTacToeGame
from games.sudoku import SudokuGame

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KP-Games")
        self.set_window_dimensions(600, 400)
        self.show_welcome_page()

    def show_welcome_page(self):
        self.clear_window()
        welcome_page = WelcomePage(self)
        welcome_page.pack(expand=True, fill="both")

    def show_menu_page(self):
        self.clear_window()
        menu_page = MenuPage(self)
        menu_page.pack(expand=True, fill="both")

    def show_tictactoe(self):
        self.clear_window()
        tictactoe_mode_selection_page = TicTacToeModeSelectionPage(self)
        tictactoe_mode_selection_page.pack(expand=True, fill="both")

    def show_tic_tac_toe_game(self, multiplayer, difficulty=None, first_player=None):
        self.clear_window()
        tic_tac_toe_game = TicTacToeGame(self, multiplayer, difficulty, first_player)
        tic_tac_toe_game.pack(expand=True, fill="both")

    def show_tictactoe_settings_page(self, multiplayer):
        self.clear_window()
        tictactoe_settings_page = TicTacToeSettingsPage(self, multiplayer)
        tictactoe_settings_page.pack(expand=True, fill="both")

    def show_sudoku_settings_page(self):
        self.clear_window()
        sudoku_settings_page = SudokuSettingsPage(self)
        sudoku_settings_page.pack(expand=True, fill="both")

    def show_sudoku_game(self, difficulty):
        self.clear_window()
        sudoku_game = SudokuGame(self, difficulty)
        sudoku_game.pack(expand=True, fill="both")

    def show_hangman_settings(self):
        self.clear_window()
        from ui.hangman_menu import HangmanSettingsPage
        settings_page = HangmanSettingsPage(self)
        settings_page.pack(expand=True, fill="both")

    def show_hangman_game(self, difficulty_settings):
        self.clear_window()
        from games.hangman import HangmanGame
        game = HangmanGame(self, difficulty_settings)
        game.pack(expand=True, fill="both")
 
    def show_number_guessing_game(self):
        self.clear_window()
        from games.number_guessing import NumberGuessingGame
        number_guessing_game = NumberGuessingGame(self)
        number_guessing_game.pack(expand=True, fill="both")

    def show_rock_paper_scissors(self):
        self.clear_window()
        from games.rock_paper_scissors import RockPaperScissorsGame
        game = RockPaperScissorsGame(self)
        game.pack(expand=True, fill="both")

    def show_snake_settings(self):
        self.clear_window()
        from ui.snake_menu import SnakeSettingsPage
        settings_page = SnakeSettingsPage(self)
        settings_page.pack(expand=True, fill="both")

    def show_snake_game(self, difficulty_settings):
        self.root.withdraw()  # Hide the Tkinter window.
        from games.snake import SnakeGame
        game = SnakeGame(
            speed=difficulty_settings.get("speed", 7),
            wrap=difficulty_settings.get("wrap", True),
            food_multiplier=difficulty_settings.get("food_multiplier", 1)
        )
        game.run()
        self.root.deiconify()  # Show Tkinter window again when done.
        self.show_menu_page()

    def show_minesweeper_settings(self):
        self.clear_window()
        from ui.minesweeper_menu import MinesweeperSettingsPage
        settings_page = MinesweeperSettingsPage(self)
        settings_page.pack(expand=True, fill="both")

    def show_minesweeper_game(self, settings):
        self.clear_window()
        from games.minesweeper import MinesweeperGame
        game = MinesweeperGame(self, rows=settings.get("rows"), cols=settings.get("cols"), mines=settings.get("mines"))
        game.pack(expand=True, fill="both")

        def show_memory_settings(self):
            self.clear_window()
            from ui.memory_menu import MemorySettingsPage
            settings_page = MemorySettingsPage(self)
            settings_page.pack(expand=True, fill="both")

        def show_memory_game(self, settings):
            self.clear_window()
            from games.memory import MemoryGame
            game = MemoryGame(self, rows=settings.get("rows"), cols=settings.get("cols"), time_limit=settings.get("time_limit"))
            game.pack(expand=True, fill="both")

    def show_memory_settings(self):
        self.clear_window()
        from ui.memory_menu import MemorySettingsPage
        settings_page = MemorySettingsPage(self)
        settings_page.pack(expand=True, fill="both")

    def show_memory_game(self, settings):
        self.clear_window()
        from games.memory import MemoryGame
        game = MemoryGame(self, rows=settings.get("rows"), cols=settings.get("cols"), time_limit=settings.get("time_limit"))
        game.pack(expand=True, fill="both")

    def set_window_dimensions_middle(self, width=600, height=400):
        self.root.geometry(f'{width}x{height}')
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def set_window_dimensions(self, width=600, height=400):
        self.root.geometry(f'{width}x{height}')
        self.root.update_idletasks()
        x = self.root.winfo_screenwidth() - width
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
