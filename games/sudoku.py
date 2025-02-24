import tkinter as tk
from tkinter import messagebox
import random

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

                cell.grid(row=r, column=c, sticky="nsew",
                          padx=(0, 5) if (c+1) % 3 == 0 else 1,
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
                if isinstance(self.cells[i][j], tk.Entry):
                    row_value = self.cells[i][j].get()
                else:
                    row_value = self.cells[i][j].cget("text")

                if isinstance(self.cells[j][i], tk.Entry):
                    col_value = self.cells[j][i].get()
                else:
                    col_value = self.cells[j][i].cget("text")

                if not row_value.isdigit() or not 1 <= int(row_value) <= 9:
                    print(f"Invalid row value at ({i}, {j})")
                    return False
                if not col_value.isdigit() or not 1 <= int(col_value) <= 9:
                    print(f"Invalid column value at ({j}, {i})")
                    return False

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
                if isinstance(self.cells[r][c], tk.Entry):
                    value = self.cells[r][c].get()
                else:
                    value = self.cells[r][c].cget("text")

                if not value.isdigit() or not 1 <= int(value) <= 9:
                    print(f"Invalid subgrid value at ({r}, {c})")
                    return False
                if value in subgrid_values:
                    print(f"Duplicate in subgrid at ({r}, {c})")
                    return False
                subgrid_values.add(value)
        return True

    def autofill_board(self):
        for r in range(9):
            for c in range(9):
                if self.puzzle_board[r][c] is None:
                    self.cells[r][c].delete(0, "end")
                    self.cells[r][c].insert(0, str(self.board[r][c]))
        self.update_hint_box("Board auto-filled!")

    def reset_board(self):
        for r in range(9):
            for c in range(9):
                if self.puzzle_board[r][c] is None:
                    self.cells[r][c].delete(0, "end")
        self.update_hint_box("Board reset!")

    def update_hint_box(self, message):
        self.hint_box.config(text=message)

    def generate_full_board(self):
        board = [[0] * 9 for _ in range(9)]
        self.fill_board(board)
        return board

    def fill_board(self, board):
        empty = self.find_empty_location(board)
        if not empty:
            return True
        row, col = empty
        random_numbers = list(range(1, 10))
        random.shuffle(random_numbers)
        for num in random_numbers:
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num
                if self.fill_board(board):
                    return True
                board[row][col] = 0
        return False

    def find_empty_location(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return (r, c)
        return None

    def generate_puzzle_board(self, difficulty):
        puzzle_board = [row[:] for row in self.board]  # copy of the full board
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
        # Check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def quit(self):
        self.app.show_sudoku_settings_page()
