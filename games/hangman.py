import tkinter as tk
from tkinter import messagebox
import random
import os

# Difficulty configuration mapping.
DIFFICULTY_SETTINGS = {
    "Easy": {"attempts": 10, "hints": 3},
    "Medium": {"attempts": 8, "hints": 2},
    "Hard": {"attempts": 6, "hints": 1},
    "Expert": {"attempts": 6, "hints": 0}
}

class HangmanGame(tk.Frame):
    """
    Hangman game page with an info panel.
    The left section shows the game (ASCII art, word, entry, and buttons).
    The right info panel displays score, attempts left, hints remaining, and guessed letters.
    """
    def __init__(self, app, difficulty_settings):
        super().__init__(app.root)
        self.app = app
        self.difficulty_settings = difficulty_settings
        self.attempts_allowed = difficulty_settings["attempts"]
        self.hints_allowed = difficulty_settings["hints"]
        self.score = 0

        # Initialize game state.
        self.words = self.load_words()
        self.new_round()

        self.ascii_stages = self.get_ascii_stages()
        self.create_widgets()
        self.update_display()

    def load_words(self):
        """Load word list from assets/words.txt if available; otherwise use a default list."""
        words = []
        try:
            with open(os.path.join("assets", "words.txt"), "r") as f:
                for line in f:
                    word = line.strip()
                    if word:
                        words.append(word)
        except Exception:
            words = ["PYTHON", "HANGMAN", "CHALLENGE", "DEVELOPER", "PROGRAM"]
        return words

    def new_round(self):
        """Start a new round by choosing a new word and resetting guesses."""
        self.word = random.choice(self.words).upper()
        self.guessed_letters = set()
        self.attempts_left = self.attempts_allowed
        self.hints_remaining = self.hints_allowed

    def get_ascii_stages(self):
        """Returns a list of ASCII art stages for Hangman."""
        stages = [
            """
             _______
             |     |
             |     
             |    
             |    
             |    
            _|_
           |   |______
           |          |
           |__________|
            """,
            """
             _______
             |     |
             |     O
             |    
             |    
             |    
            _|_
           |   |______
           |          |
           |__________|
            """,
            """
             _______
             |     |
             |     O
             |     |
             |     |
             |    
            _|_
           |   |______
           |          |
           |__________|
            """,
            """
             _______
             |     |
             |     O
             |    /|
             |     |
             |    
            _|_
           |   |______
           |          |
           |__________|
            """,
            """
             _______
             |     |
             |     O
             |    /|\\
             |     |
             |    
            _|_
           |   |______
           |          |
           |__________|
            """,
            """
             _______
             |     |
             |     O
             |    /|\\
             |     |
             |    / 
            _|_
           |   |______
           |          |
           |__________|
            """,
            """
             _______
             |     |
             |     O
             |    /|\\
             |     |
             |    / \\
            _|_
           |   |______
           |          |
           |__________|
            """
        ]
        return stages

    def create_widgets(self):
        # Configure main grid for the game frame: two columns.
        self.grid_columnconfigure(0, weight=3, uniform="main")
        self.grid_columnconfigure(1, weight=2, uniform="main")
        self.grid_rowconfigure(0, weight=1)

        # --- Left Frame: Game Area ---
        self.left_frame = tk.Frame(self)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Configure left_frame grid: assume 6 rows
        for i in range(6):
            self.left_frame.rowconfigure(i, weight=1)
        self.left_frame.columnconfigure(0, weight=1)

        # Title label.
        self.title_label = tk.Label(self.left_frame, text="Hangman", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, sticky="nsew", pady=5)

        # ASCII art label.
        self.ascii_label = tk.Label(self.left_frame, text="", font=("Courier", 12), justify="left")
        self.ascii_label.grid(row=1, column=0, sticky="nsew", pady=5)

        # Word display label.
        self.word_label = tk.Label(self.left_frame, text="", font=("Arial", 24))
        self.word_label.grid(row=2, column=0, sticky="nsew", pady=5)

        # Guess entry.
        self.guess_entry = tk.Entry(self.left_frame, font=("Arial", 18), width=5)
        self.guess_entry.grid(row=3, column=0, sticky="ew", pady=5)
        self.guess_entry.bind("<Return>", lambda event: self.guess_letter())

        # Buttons frame for horizontal arrangement.
        self.buttons_frame = tk.Frame(self.left_frame)
        self.buttons_frame.grid(row=4, column=0, sticky="ew", pady=5)
        # Configure the buttons_frame to have 4 equally sized columns.
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1, uniform="btn")

        self.guess_button = tk.Button(self.buttons_frame, text="Guess", command=self.guess_letter, font=("Arial", 16))
        self.guess_button.grid(row=0, column=0, sticky="ew", padx=2)

        self.hint_button = tk.Button(self.buttons_frame, text="Hint", command=self.give_hint, font=("Arial", 16))
        self.hint_button.grid(row=0, column=1, sticky="ew", padx=2)

        self.restart_button = tk.Button(self.buttons_frame, text="Restart", command=self.restart_round, font=("Arial", 16))
        self.restart_button.grid(row=0, column=2, sticky="ew", padx=2)

        self.back_button = tk.Button(self.buttons_frame, text="Back", command=lambda: self.app.show_menu_page(), font=("Arial", 16))
        self.back_button.grid(row=0, column=3, sticky="ew", padx=2)

        # --- Right Frame: Info Panel ---
        self.info_frame = tk.Frame(self, bd=2, relief="groove")
        self.info_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.info_frame.columnconfigure(0, weight=1)
        # Configure info_frame to have four rows.
        for i in range(4):
            self.info_frame.rowconfigure(i, weight=1)

        self.score_label = tk.Label(self.info_frame, text=f"Score: {self.score}", font=("Arial", 10))
        self.score_label.grid(row=0, column=0, sticky="nsew", pady=2)

        self.attempts_label = tk.Label(self.info_frame, text=f"Attempts left: {self.attempts_left}", font=("Arial", 10))
        self.attempts_label.grid(row=1, column=0, sticky="nsew", pady=2)

        self.hints_label = tk.Label(self.info_frame, text=f"Hints remaining: {self.hints_remaining}", font=("Arial", 10))
        self.hints_label.grid(row=2, column=0, sticky="nsew", pady=2)

        self.used_label = tk.Label(self.info_frame, text="Guessed letters: ", font=("Arial", 10),
                            wraplength=100, justify="left")
        self.used_label.grid(row=3, column=0, sticky="nsew", pady=2)

    def update_display(self):
        # Update ASCII art stage.
        stage_index = self.attempts_allowed - self.attempts_left
        stage_index = max(0, min(stage_index, len(self.ascii_stages) - 1))
        self.ascii_label.config(text=self.ascii_stages[stage_index])

        # Mask the word: show letter if guessed.
        display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_label.config(text=display_word)

        # Update info panel.
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.hints_label.config(text=f"Hints remaining: {self.hints_remaining}")
        self.used_label.config(text="Guessed letters: " + ", ".join(sorted(self.guessed_letters)))
        self.score_label.config(text=f"Score: {self.score}")

    def guess_letter(self):
        letter = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)
        if not letter.isalpha() or len(letter) != 1:
            messagebox.showinfo("Invalid", "Please enter a single letter.")
            return

        if letter in self.guessed_letters:
            messagebox.showinfo("Already guessed", f"You already guessed '{letter}'.")
            return

        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.attempts_left -= 1

        self.update_display()
        self.check_game_over()

    def give_hint(self):
        """Reveal a random unrevealed letter at the cost of one hint and one attempt."""
        if self.hints_remaining <= 0:
            messagebox.showinfo("No hints", "No hints remaining!")
            return

        not_revealed = [letter for letter in set(self.word) if letter not in self.guessed_letters]
        if not not_revealed:
            messagebox.showinfo("Hint", "All letters have been revealed!")
            return

        hint_letter = random.choice(not_revealed)
        self.guessed_letters.add(hint_letter)
        self.hints_remaining -= 1
        # Also penalize one attempt for using a hint.
        if self.attempts_left > 0:
            self.attempts_left -= 1

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        # Win condition: all letters revealed.
        if all(letter in self.guessed_letters for letter in self.word):
            self.score += 1
            messagebox.showinfo("Congratulations!", f"You've guessed the word!\nScore: {self.score}")
            self.restart_round(new_round=True)
        # Loss condition: no attempts left.
        elif self.attempts_left <= 0:
            messagebox.showinfo("Game Over", f"You've run out of attempts. The word was: {self.word}")
            self.restart_round(new_round=True)

    def restart_round(self, new_round=False):
        """Restart the current round. If new_round is True, start a fresh word without resetting the score."""
        self.new_round()
        self.update_display()

    def restart(self):
        """Restart the entire game: reset score as well as difficulty settings."""
        self.score = 0
        self.new_round()
        self.update_display()
