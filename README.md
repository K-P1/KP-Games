# KP-Games

KP-Games is a collection of eight classic and modern games built in Python. The project is designed with a modular file structure to ensure clean organization and easy maintainability. Each game is implemented either using Tkinter for GUI-based games or Pygame for more interactive ones.

## Project Structure

```
KP-Games/
│── main.py                 # Entry point for the application
│── app.py                  # Core application logic and navigation
│── ui/
│   ├── menu_page.py        # Main menu UI for game selection
│   ├── welcome_page.py     # Welcome screen UI
│   ├── sudoku_menu.py      # Sudoku difficulty selection
│   ├── tictactoe_menu.py   # Tic-Tac-Toe mode selection/settings
│   ├── hangman_menu.py     # Hangman settings page
│   ├── snake_menu.py       # Snake game settings page
│   ├── minesweeper_menu.py # Minesweeper settings page
│   ├── memory_menu.py      # Memory Card Game settings page
│── games/
│   ├── tictactoe.py        # Tic-Tac-Toe game logic/UI
│   ├── sudoku.py           # Sudoku game logic/UI
│   ├── hangman.py          # Hangman game logic/UI (using Tkinter)
│   ├── number_guessing.py  # Number Guessing game logic/UI
│   ├── rock_paper_scissors.py # Rock, Paper, Scissors game logic/UI
│   ├── snake.py            # Snake game logic (using Pygame)
│   ├── minesweeper.py      # Minesweeper game logic (using Tkinter)
│   ├── memory.py           # Memory Card Game (Matching Pairs) logic/UI
│── utils/
│   └── helpers.py          # Utility functions (if needed)
│── assets/                 # Assets like images, sounds, word lists, etc.
│── README.md               # This file
```

## Installation

1. **Requirements:**  
   - Python 3.6 or higher  
   - Tkinter (usually bundled with Python)  
   - Pygame (install via pip)

2. **Installation Steps:**  
   ```bash
   git clone https://github.com/K-P1/KP-Games.git
   cd KP-Games
   pip install -r requirements.txt
   # If a requirements.txt file is not provided, install pygame manually:
   pip install pygame
   ```

## Running the Application

To start the application, simply run:

```bash
python main.py
```

This will launch the welcome screen from where you can navigate to any game via the main menu.

## Games Overview & How to Play

### 1. Tic-Tac-Toe
- **Description:**  
  A classic Tic-Tac-Toe game. Play against another human or challenge the computer with various difficulty levels.
- **How to Play:**  
  Click on the cell where you want to place your mark (X or O). The game automatically checks for wins, draws, or prompts for a restart if needed.

### 2. Sudoku
- **Description:**  
  A number puzzle where you fill a 9x9 grid with digits so that each column, row, and 3x3 sub-grid contains all digits from 1 to 9.
- **How to Play:**  
  Use the provided UI to choose a difficulty level (which determines the number of given cells). Then, fill in the blank cells. Hints are provided based on difficulty, and you can use auto-fill or reset options as needed.

### 3. Hangman
- **Description:**  
  Guess the letters in a hidden word before you run out of attempts. A graphical version with ASCII art and a hint system.
- **How to Play:**  
  Click letters or type them in to reveal parts of the hidden word. Use hints to reveal a letter (at the cost of an attempt). The game ends when you either guess the word correctly or run out of attempts.

### 4. Number Guessing
- **Description:**  
  The computer selects a random number within a range, and you must guess it in as few attempts as possible. Hints indicate whether your guess is too high or too low.
- **How to Play:**  
  Enter your guess into the text field and press the guess button. Follow the on-screen hints until you guess the number correctly. Your attempts are recorded as your score.

### 5. Rock, Paper, Scissors
- **Description:**  
  A classic hand game where you play against the computer in a best-of-three format.
- **How to Play:**  
  Choose Rock, Paper, or Scissors using the on-screen buttons. The computer randomly selects a choice, and the round winner is determined by standard rules. The first to win two rounds wins the match. The game displays each round’s result and overall score.

### 6. Snake
- **Description:**  
  Control a snake that grows when it eats food but dies if it hits itself (and, optionally, walls in Expert mode). Difficulty levels adjust snake speed, wall wrapping behavior, and food availability.
- **How to Play:**  
  Use the arrow keys to navigate the snake. In non-Expert modes, the snake wraps around the screen; in Expert mode, hitting a wall ends the game. Use the on-screen pause and quit buttons for in-game control. A score is tracked based on food eaten.

### 7. Minesweeper
- **Description:**  
  Uncover safe cells in a grid while avoiding hidden mines. The game uses recursion to reveal large areas when an empty cell is uncovered.
- **How to Play:**  
  Click on cells to reveal what lies beneath. Numbers indicate how many adjacent mines are present. Right-click to flag potential mines. Clear all non-mine cells to win the game.

### 8. Memory Card Game (Matching Pairs)
- **Description:**  
  Flip over hidden cards two at a time to find matching pairs. A timer and scoring system challenge you to complete the board as quickly as possible.
- **How to Play:**  
  Click on a card to reveal its symbol. Then, click another card to try to find a match. If they match, they remain revealed; if not, they flip back after a short delay. Your score increases for correct matches and may decrease for wrong guesses. Complete the board before the timer runs out.

## Additional Information

- **Navigation:**  
  Use the main menu to select any game. Each game has its own settings page (if applicable) for adjusting difficulty.
  
- **Modularity:**  
  Each game’s logic and its settings UI are separated into their own modules, making it easy to update or add new games in the future.

- **Customization:**  
  You can modify the games by adjusting settings in their respective modules. For example, change difficulty levels, grid sizes, speeds, or scoring rules.

## Acknowledgments

- Special thanks to all myself for completing this project.