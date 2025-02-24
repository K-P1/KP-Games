import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.create_widgets()
        self.reset_match_info()

    def create_widgets(self):
        # Main grid: two columns: left (game screen) and right (info panel)
        self.grid_columnconfigure(0, weight=3, uniform="main")
        self.grid_columnconfigure(1, weight=2, uniform="main")
        self.grid_rowconfigure(0, weight=1)

        # ----------------- Left Frame: Game Screen -----------------
        self.left_frame = tk.Frame(self, bd=2, relief="sunken")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        # Use grid in left_frame with two columns for the mini panels
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(2, weight=1)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=3)  
        self.left_frame.grid_rowconfigure(2, weight=1)
        self.left_frame.grid_rowconfigure(3, weight=1)

        # Title
        self.title_label = tk.Label(self.left_frame, text="Rock, Paper, Scissors", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Mini panels row (row=1): "You" and "Computer"
        self.user_panel = tk.Frame(self.left_frame, bd=1, relief="groove")
        self.user_panel.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.user_label = tk.Label(self.user_panel, text="You", font=("Arial", 12))
        self.user_label.pack(pady=5)
        self.user_choice_label = tk.Label(self.user_panel, text="", font=("Arial", 18))
        self.user_choice_label.pack(pady=25)

        self.computer_panel = tk.Frame(self.left_frame, bd=1, relief="groove")
        self.computer_panel.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.computer_label = tk.Label(self.computer_panel, text="Computer", font=("Arial", 12))
        self.computer_label.pack(pady=5)
        self.computer_choice_label = tk.Label(self.computer_panel, text="", font=("Arial", 18))
        self.computer_choice_label.pack(pady=25)

        # Row for the three choice buttons
        self.choices_frame = tk.Frame(self.left_frame)
        self.choices_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        # Configure three equal columns
        for i in range(3):
            self.choices_frame.grid_columnconfigure(i, weight=1, uniform="choice")
        self.rock_button = tk.Button(self.choices_frame, text="Rock", font=("Arial", 16),
                                     command=lambda: self.play_round("Rock"))
        self.rock_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.paper_button = tk.Button(self.choices_frame, text="Paper", font=("Arial", 16),
                                      command=lambda: self.play_round("Paper"))
        self.paper_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.scissors_button = tk.Button(self.choices_frame, text="Scissors", font=("Arial", 16),
                                         command=lambda: self.play_round("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Row for the bottom buttons (Restart and Back)
        self.bottom_frame = tk.Frame(self.left_frame)
        self.bottom_frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.bottom_frame.grid_columnconfigure(0, weight=1, uniform="bottom")
        self.bottom_frame.grid_columnconfigure(1, weight=1, uniform="bottom")
        self.restart_button = tk.Button(self.bottom_frame, text="Restart", font=("Arial", 14),
                                        command=self.restart_game)
        self.restart_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.back_button = tk.Button(self.bottom_frame, text="Back", font=("Arial", 14),
                                     command=lambda: self.app.show_menu_page())
        self.back_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # ----------------- Right Frame: Info Panel -----------------
        self.info_frame = tk.Frame(self, bd=2, relief="groove")
        self.info_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_rowconfigure(0, weight=1)
        # Use a Text widget to record round info (it will wrap automatically)
        self.info_text = tk.Text(self.info_frame, wrap="word", font=("Arial", 12), state="disabled")
        self.info_text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def reset_match_info(self):
        # Clear mini panels
        self.user_choice_label.config(text="")
        self.computer_choice_label.config(text="")
        # Clear info panel
        self.info_text.config(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.config(state="disabled")
        # Reset scores
        self.user_score = 0
        self.computer_score = 0

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)
        # Update mini panels with the current round's choices
        self.user_choice_label.config(text=user_choice)
        self.computer_choice_label.config(text=computer_choice)
        # Determine winner for this round
        result = self.determine_winner(user_choice, computer_choice)
        round_info = f"You: {user_choice} | Computer: {computer_choice}\nResult: {result}\n"
        # Append round info to the info panel
        self.info_text.config(state="normal")
        self.info_text.insert(tk.END, round_info + "\n")
        self.info_text.see(tk.END)
        self.info_text.config(state="disabled")
        self.check_best_of_three()

    def determine_winner(self, user, computer):
        if user == computer:
            return "Tie"
        if ((user == "Rock" and computer == "Scissors") or
            (user == "Scissors" and computer == "Paper") or
            (user == "Paper" and computer == "Rock")):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def check_best_of_three(self):
        score_info = f"Current Score -> You: {self.user_score} | Computer: {self.computer_score}\n"
        self.info_text.config(state="normal")
        self.info_text.insert(tk.END, score_info + "\n")
        self.info_text.see(tk.END)
        self.info_text.config(state="disabled")
        if self.user_score == 2 or self.computer_score == 2:
            if self.user_score > self.computer_score:
                final_message = f"Congratulations! You win best-of-three!\nFinal Score: {self.user_score} - {self.computer_score}"
            else:
                final_message = f"Computer wins best-of-three.\nFinal Score: {self.user_score} - {self.computer_score}"
            messagebox.showinfo("Game Over", final_message)
            self.reset_match_info()

    def restart_game(self):
        self.reset_match_info()
