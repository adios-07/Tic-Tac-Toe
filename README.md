# Tic-Tac-Toe AI Showdown 🤖⚔️

Welcome to my advanced Tic-Tac-Toe project! This isn't just a simple game; it's an arena where you can challenge a Python-powered bot with multiple levels of intelligence. From a completely random opponent to an unbeatable AI that thinks moves ahead, this project is a deep dive into game logic and artificial intelligence.

## ✨ Features

* **Play in Your Terminal:** A clean, easy-to-read command-line interface.
* **Choose Your Symbol:** Start the game as either 'X' (first move) or 'O'.
* **Multiple AI Difficulties:** Test your skills against three distinct bot personalities.
* **Unbeatable AI:** Challenge the "Hard" difficulty bot that uses the Minimax algorithm to play a perfect game, every time.
* **Clean & Modular Code:** The game logic and the bot's "brain" are separated into two different files for clarity and scalability.

## 📂 Project Structure

The project is split into two main files to keep things organized:

* `tictactoe.py`: This is the main game engine. It handles drawing the board, getting player input, and managing the game loop.
* `Smart_Bot.py`: This file contains the "brain" of the AI. It houses the logic for all three difficulty levels, from the simple random picker to the complex Minimax algorithm.

## 🚀 How to Play

Getting the game running is simple. As long as you have Python installed, you're ready to go.

1.  **Clone or Download:** Get the `tictactoe.py` and `Smart_Bot.py` files and place them in the same folder.
2.  **Open Your Terminal:** Navigate to the folder where you saved the files.
3.  **Run the Game:** Type the following command and press Enter:


    ```bash
    python tictactoe.py 
    ```
    or
    ```bash
    py tictactoe.py 
    ```
5.  **Follow the Prompts:** The game will ask you to choose your symbol ('X' or 'O') and the difficulty level. Enjoy the challenge!

## 🧠 The Bots: A Look Inside the AI

This project features three different AI opponents, each with its own strategy.

### 🤖 Easy

The "Easy" bot is your classic, unpredictable opponent. It doesn't have a strategy; it simply picks a random empty square on the board for its move. It's a great way to learn the game, but you'll probably beat it every time.

### 🤔 Medium

The "Medium" bot is much smarter. It thinks one move ahead with two simple, powerful rules:

1.  **"Can I win?"**: It scans the board to see if it can place a piece and win the game immediately.
2.  **"Do I need to block?"**: If it can't win, it checks if the player is about to win on their next turn and blocks them.
    If neither of these conditions is met, it falls back to making a random move. This bot provides a decent challenge and will punish obvious mistakes.

### 🏆 Hard (Unbeatable)

The "Hard" bot is the main event. It uses the **Minimax algorithm** to play a perfect game.

**How does it work?**
In simple terms, the bot looks at every possible move it can make. For each move, it simulates the entire rest of the game, assuming the player will also play perfectly to counter it. It explores this "game tree" of all possible futures to find the path that guarantees the best possible outcome for itself (a win, or a draw if a win isn't possible). It is mathematically impossible to beat this bot—the best you can hope for is a draw!
