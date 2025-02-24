import tkinter as tk
from tkinter import messagebox
import random

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

        # Offensive checks
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

        # Defensive checks
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

        # Otherwise pick a random move
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
