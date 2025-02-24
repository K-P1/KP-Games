import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="Guess the Number (1-100)", font=("Arial", 24))
        title.pack(pady=20)

        self.entry = tk.Entry(self, font=("Arial", 18))
        self.entry.pack(pady=10)

        self.feedback_label = tk.Label(self, text="", font=("Arial", 18))
        self.feedback_label.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        guess_button = tk.Button(button_frame, text="Guess", command=self.check_guess, font=("Arial", 16), width=10)
        guess_button.pack(side=tk.LEFT, padx=5)

        restart_button = tk.Button(button_frame, text="Restart", command=self.restart, font=("Arial", 16), width=10)
        restart_button.pack(side=tk.LEFT, padx=5)

        back_button = tk.Button(button_frame, text="Back", command=self.go_back, font=("Arial", 16), width=10)
        back_button.pack(side=tk.LEFT, padx=5)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.target:
            self.feedback_label.config(text="Too low! Try again.")
        elif guess > self.target:
            self.feedback_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
            self.restart()

    def restart(self):
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def go_back(self):
        self.app.show_menu_page()
