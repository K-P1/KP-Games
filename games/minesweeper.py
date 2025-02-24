import tkinter as tk
from tkinter import messagebox
import random

class MinesweeperGame(tk.Frame):
    def __init__(self, app, rows=9, cols=9, mines=10):
        super().__init__(app.root)
        self.app = app
        self.rows = rows
        self.cols = cols
        self.total_mines = mines
        self.create_board()
        self.create_widgets()

    def create_board(self):
        # Initialize board data.
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.revealed = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        # Place mines.
        count = 0
        while count < self.total_mines:
            r = random.randrange(self.rows)
            c = random.randrange(self.cols)
            if self.board[r][c] == -1:
                continue
            self.board[r][c] = -1
            count += 1
            # Increase adjacent cells’ numbers.
            for i in range(max(0, r-1), min(self.rows, r+2)):
                for j in range(max(0, c-1), min(self.cols, c+2)):
                    if self.board[i][j] != -1:
                        self.board[i][j] += 1

    def create_widgets(self):
        # Clear any previous widgets.
        for widget in self.winfo_children():
            widget.destroy()
        #dynamic font size
        base_font_size = 12
        font_size = max(8, base_font_size - self.rows // 2)
        # Use grid layout for the board.
        for r in range(self.rows):
            self.grid_rowconfigure(r, weight=1)
            for c in range(self.cols):
                self.grid_columnconfigure(c, weight=1)
                btn = tk.Button(self, text="", font=("Arial", font_size),
                                command=lambda r=r, c=c: self.on_click(r, c))
                btn.bind("<Button-3>", lambda event, r=r, c=c: self.on_right_click(r, c))
                btn.grid(row=r, column=c, sticky="nsew")
                self.buttons[r][c] = btn
        # Create a frame at the bottom for Restart and Back buttons.
        bottom_frame = tk.Frame(self)
        bottom_frame.grid(row=self.rows, column=0, columnspan=self.cols, sticky="ew")
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)
        restart_button = tk.Button(bottom_frame, text="Restart", font=("Arial", 14),
                                   command=self.restart_game)
        restart_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        back_button = tk.Button(bottom_frame, text="Back", font=("Arial", 14),
                                command=lambda: self.app.show_menu_page())
        back_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    def on_click(self, r, c):
        if self.revealed[r][c]:
            return
        self.reveal_cell(r, c)
        if self.board[r][c] == -1:
            self.game_over()
        elif self.check_win():
            messagebox.showinfo("Congratulations", "You win!")
            self.restart_game()

    def reveal_cell(self, r, c):
        # Base cases.
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return
        if self.revealed[r][c]:
            return
        self.revealed[r][c] = True
        btn = self.buttons[r][c]
        if self.board[r][c] == -1:
            btn.config(text="*", bg="red")
        elif self.board[r][c] == 0:
            btn.config(text="", relief="sunken", bg="lightgrey")
            # Recursively reveal neighboring cells.
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if i == r and j == c:
                        continue
                    self.reveal_cell(i, j)
        else:
            btn.config(text=str(self.board[r][c]), relief="sunken", bg="lightgrey")

    def on_right_click(self, r, c):
        # Toggle flag on right-click if cell is not revealed.
        if not self.revealed[r][c]:
            btn = self.buttons[r][c]
            current = btn.cget("text")
            if current == "F":
                btn.config(text="")
            else:
                btn.config(text="F")

    def game_over(self):
        # Reveal all mines.
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    self.buttons[r][c].config(text="*", bg="red")
        messagebox.showinfo("Game Over", "You hit a mine!")
        self.restart_game()

    def check_win(self):
        # Win if every non-mine cell is revealed.
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != -1 and not self.revealed[r][c]:
                    return False
        return True

    def restart_game(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c].destroy()
        self.create_board()
        self.create_widgets()
