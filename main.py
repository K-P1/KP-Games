import tkinter as tk
from tkinter import messagebox
import random

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

class WelcomePage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        WelcomePage_L1= tk.Label(self, text="Welcome to KP-Games", font=("Arial", 36))
        WelcomePage_B1= tk.Button(self, text="Login", command=self.login, width=25, height=3)
        WelcomePage_B2= tk.Button(self, text="Sign Up", command=self.sign_up, width=25, height=3)
        WelcomePage_B3= tk.Button(self, text="Proceed as Guest", command=self.proceed_as_guest, width=25, height=3)
        WelcomePage_B4= tk.Button(self, text="Exit", command=self.quit, width=25, height=3)
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

class MenuPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        MenuPage_L1= tk.Label(self, text="Select a Game", font=("Arial", 36))
        MenuPage_B1= tk.Button(self, text="Tic-Tac-Toe", command=self.start_tictactoe,width=20,height=12)
        MenuPage_B2= tk.Button(self, text="Sudoku", command=self.start_sudoku,width=20,height=12)
        MenuPage_B3= tk.Button(self, text="Back", command=self.back, width=20,height=12)
        MenuPage_L1.grid(row=0,column=0,columnspan=3)
        MenuPage_B1.grid(row=1,column=0)
        MenuPage_B2.grid(row=1,column=1)
        MenuPage_B3.grid(row=1,column=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
    
    def start_tictactoe(self):
        self.app.show_tictactoe()
    
    def start_sudoku(self):
        self.app.show_sudoku_settings_page()
    
    def back(self):
        self.app.show_welcome_page()

class TicTacToeGame(tk.Frame):
    def __init__(self, app, multiplayer, difficulty, first_player):
        super().__init__(app.root)
        self.app = app
        self.board = [None] * 9
        self.current_player = "X" if first_player == "Player 1" else "O"
        self.multiplayer = multiplayer
        self.difficulty = difficulty
        self.first_player = first_player
        self.create_widgets()
        if not multiplayer and self.current_player == "O":
            self.computer_move()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            self.grid_rowconfigure(i, weight=2, uniform="row")
            self.grid_columnconfigure(i, weight=1, uniform="col")
        for i in range(9):
            button = tk.Button(self, text="", font=("Arial", 36),
                            command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3, sticky="nsew", padx=5, pady=5)
            self.buttons.append(button)
        tk.Button(self, text="Restart", command=self.restart).grid(row=3, column=0, sticky="nswe", padx=5, pady=5)
        tk.Button(self, text="Quit", command=self.quit).grid(row=3, column=2, sticky="nswe", padx=5, pady=5)
        self.grid_rowconfigure(3, weight=1)

    def make_move(self, index):
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.restart()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.restart()
            else:
                if not self.multiplayer:
                    if self.current_player == "X":
                        self.current_player = "O"
                        self.computer_move()
                    else:
                        self.current_player = "X"
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"

    def easy_ai_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell is None]
        if empty_cells:
            index = random.choice(empty_cells)
            self.make_move(index)

    def medium_ai_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell is None]
        for combo in self.get_winning_combinations():
            if self.board[combo[0]] == self.board[combo[1]] == "O" and self.board[combo[2]] is None:
                self.make_move(combo[2])
                return
            if self.board[combo[0]] == self.board[combo[2]] == "O" and self.board[combo[1]] is None:
                self.make_move(combo[1])
                return
            if self.board[combo[1]] == self.board[combo[2]] == "O" and self.board[combo[0]] is None:
                self.make_move(combo[0])
                return
        for combo in self.get_winning_combinations():
            if self.board[combo[0]] == self.board[combo[1]] == "X" and self.board[combo[2]] is None:
                self.make_move(combo[2])
                return
            if self.board[combo[0]] == self.board[combo[2]] == "X" and self.board[combo[1]] is None:
                self.make_move(combo[1])
                return
            if self.board[combo[1]] == self.board[combo[2]] == "X" and self.board[combo[0]] is None:
                self.make_move(combo[0])
                return
        if empty_cells:
            index = random.choice(empty_cells)
            self.make_move(index)

    def hard_ai_move(self):
        if self.board.count(None) == 9:
            first_move = random.choice([0, 2, 4, 6, 8])
            self.make_move(first_move)
            return
        move = self.find_winning_move("O")
        if move is not None:
            self.make_move(move)
            return
        move = self.find_winning_move("X")
        if move is not None:
            self.make_move(move)
            return
        move = self.find_best_move()
        if move is not None:
            self.make_move(move)

    def expert_ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] is None:
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = None
                if score > best_score:
                    best_score = score
                    best_move = i
        if best_move is not None:
            self.make_move(best_move)

    def minimax(self, board, depth, is_maximizing):
        if self.check_win_condition("O"):
            return 1
        elif self.check_win_condition("X"):
            return -1
        elif None not in board:
            return 0
        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] is None:
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = None
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] is None:
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = None
                    best_score = min(score, best_score)
            return best_score

    def computer_move(self):
        if self.difficulty == "Easy":
            self.easy_ai_move()
        elif self.difficulty == "Medium":
            self.medium_ai_move()
        elif self.difficulty == "Hard":
            self.hard_ai_move()
        elif self.difficulty == "Expert":
            self.expert_ai_move()

    def check_win_condition(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def find_winning_move(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                                (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                                (0, 4, 8), (2, 4, 6)]
        
        for combo in winning_combinations:
            line = [self.board[i] for i in combo]
            if line.count(player) == 2 and line.count(None) == 1:
                return combo[line.index(None)]
        return None

    def find_best_move(self):
        corners = [0, 2, 6, 8]
        edges = [1, 3, 5, 7]
        empty_corners = [i for i in corners if self.board[i] is None]
        if empty_corners:
            return random.choice(empty_corners)
        empty_edges = [i for i in edges if self.board[i] is None]
        if empty_edges:
            return random.choice(empty_edges)
        return None

    def check_win(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] is not None:
                return True
        return False
    
    def get_winning_combinations(self):
        return [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]

    def restart(self):
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X" if self.first_player == "Player 1" else "O"
        if not self.multiplayer and self.current_player == "O":
            self.computer_move()

    def quit(self):
        self.app.show_tictactoe()

class TicTacToeModeSelectionPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        TicTacToeModeSelectionPage_L1= tk.Label(self, text="Select Game Mode", font=("Arial", 36))
        TicTacToeModeSelectionPage_B1= tk.Button(self, text="Multiplayer", command=self.start_multiplayer, width=20, height=5)
        TicTacToeModeSelectionPage_B2= tk.Button(self, text="Single Player", command=self.start_single_player, width=20, height=5)
        TicTacToeModeSelectionPage_B3= tk.Button(self, text="Back", command=self.back, width=20, height=5)
        TicTacToeModeSelectionPage_L1.grid(row=0,column=0,columnspan=3)
        TicTacToeModeSelectionPage_B1.grid(row=1,column=0)
        TicTacToeModeSelectionPage_B2.grid(row=1,column=1)
        TicTacToeModeSelectionPage_B3.grid(row=1,column=2)
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
        TicTacToeSettingsPage_L0= tk.Label(self, text="Game Settings", font=("Arial", 36))
        TicTacToeSettingsPage_L0.grid(row=0,column=0,columnspan=2)
        if not self.multiplayer:
            TicTacToeSettingsPage_L1= tk.Label(self, text="Select Difficulty:")
            self.difficulty_var = tk.StringVar(value="Easy")
            TicTacToeSettingsPage_R1= tk.Radiobutton(self, text="Easy", variable=self.difficulty_var, value="Easy")
            TicTacToeSettingsPage_R2= tk.Radiobutton(self, text="Medium", variable=self.difficulty_var, value="Medium")
            TicTacToeSettingsPage_R3= tk.Radiobutton(self, text="Hard", variable=self.difficulty_var, value="Hard")
            TicTacToeSettingsPage_R4= tk.Radiobutton(self, text="Expert (Beta)", variable=self.difficulty_var, value="Expert")

            TicTacToeSettingsPage_L1.grid(row=1,column=0,columnspan=2)
            TicTacToeSettingsPage_R1.grid(row=2,column=0,columnspan=2, sticky='w',padx=15)
            TicTacToeSettingsPage_R2.grid(row=3,column=0,columnspan=2, sticky='w',padx=15)
            TicTacToeSettingsPage_R3.grid(row=4,column=0,columnspan=2, sticky='w',padx=15)
            TicTacToeSettingsPage_R4.grid(row=5,column=0,columnspan=2, sticky='w',padx=15)

        else:
            self.difficulty_var = None
        TicTacToeSettingsPage_L2= tk.Label(self, text="Who Goes First:")
        self.first_player_var = tk.StringVar(value="Player 1")
        TicTacToeSettingsPage_R5= tk.Radiobutton(self, text="Player 1 (X)", variable=self.first_player_var, value="Player 1")
        TicTacToeSettingsPage_R6= tk.Radiobutton(self, text="Player 2 (O)", variable=self.first_player_var, value="Player 2")
        TicTacToeSettingsPage_B1= tk.Button(self, text="Start Game", command=self.start_game, width=15)
        TicTacToeSettingsPage_B2= tk.Button(self, text="Back", command=self.back, width=15)
        TicTacToeSettingsPage_L2.grid(row=6,column=0,columnspan=2)
        TicTacToeSettingsPage_R5.grid(row=7,column=0,columnspan=2, sticky='w',padx=15)
        TicTacToeSettingsPage_R6.grid(row=8,column=0,columnspan=2, sticky='w',padx=15)
        TicTacToeSettingsPage_B1.grid(row=9,column=0)
        TicTacToeSettingsPage_B2.grid(row=9,column=1)
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
        self.app.show_tic_tac_toe_game(multiplayer=self.multiplayer, difficulty=difficulty, first_player=first_player)

    def back(self):
        self.app.show_tictactoe()

class SudokuSettingsPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        
        SudokuSettingsPage_L1 = tk.Label(self, text="Select Difficulty Level:", font=("Arial", 36))
        self.difficulty_var = tk.StringVar(value="easy")
        SudokuSettingsPage_R1 = tk.Radiobutton(self, text="Easy", variable=self.difficulty_var, value="easy",command=self.show_difficulty_info)
        SudokuSettingsPage_R2 = tk.Radiobutton(self, text="Medium", variable=self.difficulty_var, value="medium",command=self.show_difficulty_info)
        SudokuSettingsPage_R3 = tk.Radiobutton(self, text="Hard", variable=self.difficulty_var, value="hard",command=self.show_difficulty_info)
        SudokuSettingsPage_R4 = tk.Radiobutton(self, text="Expert", variable=self.difficulty_var, value="expert",command=self.show_difficulty_info)
        SudokuSettingsPage_B1 = tk.Button(self, text="Start Game", command=self.start_game, width=15)
        SudokuSettingsPage_B2 = tk.Button(self, text="Back", command=self.back, width=15)
        self.info_label = tk.Label(self, text="", height= 2, font=("Arial", 16))

        SudokuSettingsPage_L1.grid(row=0,column=0, columnspan=2, sticky='we')
        SudokuSettingsPage_R1.grid(row=1,column=0, sticky='w', padx=15)
        SudokuSettingsPage_R2.grid(row=2,column=0, sticky='w', padx=15)
        SudokuSettingsPage_R3.grid(row=3,column=0, sticky='w', padx=15)
        SudokuSettingsPage_R4.grid(row=4,column=0, sticky='w', padx=15)
        SudokuSettingsPage_B2.grid(row=5,column=0, sticky='w', padx=15)
        SudokuSettingsPage_B1.grid(row=5,column=1, sticky='e', padx=15)
        self.info_label.grid(row=6,column=0, columnspan=2, sticky='we')

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
        difficulty = self.difficulty_var.get()  # Get selected difficulty
        self.app.show_sudoku_game(difficulty)  # Pass difficulty to SudokuGame

    def back(self):
        self.app.show_menu_page()

class SudokuGame(tk.Frame):
    def __init__(self, app, difficulty):
        super().__init__(app.root)
        self.app = app
        self.difficulty = difficulty
        
        # Initialize hints_enabled before generating the board
        self.hints_enabled = difficulty in ["easy", "medium"]
        
        self.board = self.generate_full_board()
        self.puzzle_board = self.generate_puzzle_board(difficulty)
        self.create_widgets()

    def create_widgets(self):
        # Hint box
        self.hint_box = tk.Label(self, text="", anchor="w", justify="left", bg="lightgray", font=('Arial', 20))
        self.hint_box.grid(row=9, column=0, columnspan=5, rowspan=2, sticky="nsew")

        # Reset button
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_board)
        self.reset_button.grid(row=9, column=7, columnspan=2, padx=15, pady=2, sticky='wens')

        # Quit button
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=10, column=7, columnspan=2, padx=15, pady=2, sticky='wens')

        # Fill button
        self.autofill_button = tk.Button(self, text="Auto-Fill", command=self.autofill_board)
        self.autofill_button.grid(row=9, column=5, columnspan=2, rowspan=2, sticky="wens", padx=15, pady=2)

        # Create the Sudoku grid
        for i in range(9):
            self.grid_rowconfigure(i, weight=1, uniform="row")
            self.grid_columnconfigure(i, weight=1, uniform="col")
        self.cells = []
        for r in range(9):
            row_cells = []
            for c in range(9):
                cell_value = self.puzzle_board[r][c]
                
                if cell_value is not None:
                    # Use a label for prefilled cells
                    cell = tk.Label(self, text=str(cell_value), font=('Arial', 18), bg="lightgray", width=9)
                else:
                    cell = tk.Entry(self, width=9, justify="center", font=('Arial', 17))
                    cell.bind("<KeyRelease>", lambda e, row=r, col=c: self.on_key_release(e, row, col))
                
                cell.grid(row=r, column=c, sticky="nsew", padx=(0, 5) if (c+1) % 3 == 0 else 1,
                        pady=(0, 5) if (r+1) % 3 == 0 else 1)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def check_completion(self):
        print("Checking if the board is complete...")

        # Check rows and columns
        for i in range(9):
            row_values = set()
            col_values = set()

            for j in range(9):
                # Get the value of the cell in row and column
                if isinstance(self.cells[i][j], tk.Entry):
                    row_value = self.cells[i][j].get()
                else:
                    row_value = self.cells[i][j].cget("text")
                
                if isinstance(self.cells[j][i], tk.Entry):
                    col_value = self.cells[j][i].get()
                else:
                    col_value = self.cells[j][i].cget("text")

                # Check if they are digits and within the valid range
                if not row_value.isdigit() or not 1 <= int(row_value) <= 9:
                    print(f"Invalid row value at ({i}, {j})")
                    return False
                if not col_value.isdigit() or not 1 <= int(col_value) <= 9:
                    print(f"Invalid column value at ({j}, {i})")
                    return False

                # Add to the set, and if we have duplicates, return False
                if row_value in row_values or col_value in col_values:
                    print(f"Duplicate in row or column at ({i}, {j}) or ({j}, {i})")
                    return False

                row_values.add(row_value)
                col_values.add(col_value)

        # Check 3x3 subgrids
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                if not self.check_subgrid(box_row, box_col):
                    return False

        messagebox.showinfo("Congratulations!", "You've completed the puzzle!")
        print("Board is valid and complete!")
        return True

    def on_key_release(self, event, row, col):
        value = event.widget.get()
        
        # Always check for invalid characters
        if not value.isdigit() or not 1 <= int(value) <= 9:
            self.update_hint_box("Enter a valid number (1-9)") if value != '' else self.update_hint_box('')
            return
        
        # Only show correctness hints if hints are enabled for the difficulty
        if self.hints_enabled:
            if self.is_valid_move(self.puzzle_board, row, col, int(value)):
                self.update_hint_box("Correct move!")
            else:
                self.update_hint_box("Wrong move!")

        # Check for completion after each move
        self.check_completion()

    def check_subgrid(self, start_row, start_col):
        subgrid_values = set()

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                # Check if the cell is an Entry or Label and get the value accordingly
                if isinstance(self.cells[r][c], tk.Entry):
                    value = self.cells[r][c].get()
                else:
                    value = self.cells[r][c].cget("text")
                
                # Check if the value is a valid digit
                if not value.isdigit() or not 1 <= int(value) <= 9:
                    print(f"Invalid subgrid value at ({r}, {c})")
                    return False

                # Check for duplicates in the subgrid
                if value in subgrid_values:
                    print(f"Duplicate in subgrid at ({r}, {c})")
                    return False

                subgrid_values.add(value)

        return True
    
    def autofill_board(self):
        """Automatically fill the board with correct numbers."""
        for r in range(9):
            for c in range(9):
                if self.puzzle_board[r][c] is None:
                    self.cells[r][c].delete(0, "end")
                    self.cells[r][c].insert(0, str(self.board[r][c]))
        self.update_hint_box("Board auto-filled!")

    def reset_board(self):
        """Reset the board to the initial puzzle state."""
        for r in range(9):
            for c in range(9):
                if self.puzzle_board[r][c] is None:
                    self.cells[r][c].delete(0, "end")
        self.update_hint_box("Board reset!")

    def update_hint_box(self, message):
        self.hint_box.config(text=message)

    def generate_full_board(self):
        """Generate a fully solved Sudoku board using a backtracking algorithm."""
        board = [[0] * 9 for _ in range(9)]
        self.fill_board(board)
        return board
    
    def fill_board(self, board):
        """Recursive backtracking to fill the Sudoku board."""
        empty = self.find_empty_location(board)
        if not empty:
            return True  # Board is complete
        row, col = empty
        random_numbers = list(range(1, 10))
        random.shuffle(random_numbers)

        for num in random_numbers:
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num
                if self.fill_board(board):
                    return True
                board[row][col] = 0  # Backtrack

        return False

    def find_empty_location(self, board):
        """Find an empty location on the board (cell with 0)."""
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return (r, c)
        return None

    def generate_puzzle_board(self, difficulty):
        """Generates a puzzle board by removing numbers from the full board based on difficulty."""
        puzzle_board = [row[:] for row in self.board]  # Make a copy of the full board

        # Remove numbers from the board based on difficulty level
        if difficulty == "easy":
            empty_cells = 2
        elif difficulty == "medium":
            empty_cells = 25
        elif difficulty == "hard":
            empty_cells = 35
        elif difficulty == "expert":
            empty_cells = 55

        while empty_cells > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if puzzle_board[row][col] is not None:
                puzzle_board[row][col] = None
                empty_cells -= 1

        return puzzle_board

    def is_valid_move(self, board, row, col, num):
        # Check row, column, and 3x3 subgrid
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def quit(self):
        self.app.show_sudoku_settings_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()