import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame(tk.Frame):
    def __init__(self, app, rows=4, cols=4, time_limit=120):
        super().__init__(app.root)
        self.app = app
        self.rows = rows
        self.cols = cols
        self.total_cards = rows * cols
        # Ensure we have an even number of cards.
        if self.total_cards % 2 != 0:
            self.total_cards += 1
        self.time_limit = time_limit  # in seconds
        self.elapsed_time = 0
        self.score = 0
        self.first_selection = None
        self.lock = False
        self.create_cards()
        self.create_widgets()
        self.start_timer()

    def create_cards(self):
        # Create a list of pairs.
        pairs = list(range(1, self.total_cards // 2 + 1)) * 2
        random.shuffle(pairs)
        self.cards = pairs  # List of values for each card.
        self.revealed = [False] * self.total_cards  # Track which cards are permanently revealed.

    def create_widgets(self):
        # Create a frame for the grid.
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(expand=True, fill="both")
        # Configure grid rows and columns.
        for r in range(self.rows):
            self.grid_frame.grid_rowconfigure(r, weight=1)
        for c in range(self.cols):
            self.grid_frame.grid_columnconfigure(c, weight=1)
        # Create card buttons.
        self.buttons = []
        for i in range(self.total_cards):
            btn = tk.Button(self.grid_frame, text="", font=("Arial", 16),
                            command=lambda i=i: self.on_card_click(i))
            btn.bind("<Button-3>", lambda event, i=i: self.on_right_click(i))
            btn.grid(row=i // self.cols, column=i % self.cols, sticky="nsew", padx=2, pady=2)
            self.buttons.append(btn)

        # Create an info panel below the grid.
        info_frame = tk.Frame(self)
        info_frame.pack(fill="x", pady=5)
        self.timer_label = tk.Label(info_frame, text="Time: 0 s", font=("Arial", 14))
        self.timer_label.pack(side="left", padx=10)
        self.score_label = tk.Label(info_frame, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(side="left", padx=10)
        restart_button = tk.Button(info_frame, text="Restart", font=("Arial", 14), command=self.restart_game)
        restart_button.pack(side="right", padx=10)
        back_button = tk.Button(info_frame, text="Back", font=("Arial", 14),
                                command=lambda: self.app.show_menu_page())
        back_button.pack(side="right", padx=10)

    def on_card_click(self, index):
        if self.lock or self.revealed[index]:
            return
        # Reveal card.
        self.buttons[index].config(text=str(self.cards[index]), state="disabled", relief="sunken")
        if self.first_selection is None:
            self.first_selection = index
        else:
            self.lock = True
            self.after(800, self.check_match, self.first_selection, index)
            self.first_selection = None

    def on_right_click(self, index):
        # (Optional: implement flagging here if desired.)
        pass

    def check_match(self, i1, i2):
        if self.cards[i1] == self.cards[i2]:
            # They match – mark as revealed and award score.
            self.revealed[i1] = True
            self.revealed[i2] = True
            self.score += 10
        else:
            # They don't match – flip back and deduct score.
            self.buttons[i1].config(text="", state="normal", relief="raised")
            self.buttons[i2].config(text="", state="normal", relief="raised")
            self.score -= 2
        self.update_score()
        self.lock = False
        if all(self.revealed):
            messagebox.showinfo("Congratulations", f"You matched all pairs!\nFinal Score: {self.score}")
            self.restart_game()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def start_timer(self):
        self.elapsed_time = 0
        self.update_timer()

    def update_timer(self):
        self.elapsed_time += 1
        self.timer_label.config(text=f"Time: {self.elapsed_time} s")
        if self.elapsed_time < self.time_limit:
            self.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time Up", f"Time's up!\nFinal Score: {self.score}")
            self.restart_game()

    def restart_game(self):
        # Destroy current widgets and reinitialize the game.
        for btn in self.buttons:
            btn.destroy()
        self.grid_frame.destroy()
        self.destroy()
        self.app.show_memory_game({"rows": self.rows, "cols": self.cols, "time_limit": self.time_limit})
