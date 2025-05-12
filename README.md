# 🧠 Tic-Tac-Toe with Alpha-Beta Pruning AI

This project is a Python implementation of the classic **Tic-Tac-Toe** game where a human player plays against an AI. The AI uses the **Alpha-Beta Pruning** technique, a refined version of the Minimax algorithm, to determine its optimal moves efficiently. The program also includes a basic heuristic evaluation function and allows for configurable search depth.

---

## 🚀 Features

- 3x3 interactive console-based Tic-Tac-Toe game.
- Human vs AI gameplay.
- AI uses **Alpha-Beta Pruning** to reduce the number of game states it needs to explore.
- Depth-limited search to manage computation time.
- Simple yet informative board rendering.
- Reference board for intuitive user input.
- Statistics on number of game states explored.

---

## 🧠 AI Strategy

The AI ('O') implements a limited-depth **Alpha-Beta Pruning** strategy to optimize its decisions. The following logic is used:

- `alpha_beta_pruning()` is the core recursive function that explores the game tree.
- A basic **heuristic function** estimates the quality of non-terminal states at the depth limit.
- The AI maximizes its score (`'O'`), while minimizing the opponent’s (`'X'`).
- A fixed **depth limit** (default: `3`) is applied to control search time.

---

## 📁 File Structure

```
tic_tac_toe_ai.py       # Main game file containing all logic and AI
```

---

## 📷 Game Preview

```
Reference Board:
  1 | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9

Current Board:
    |   |  
 -----------
    |   |  
 -----------
    |   |  

Enter move (1-9):
```

---

## 🛠️ How to Run

### ✅ Requirements
- Python 3.6 or later

### ▶️ Execution

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/tic-tac-toe-ai.git
    cd tic-tac-toe-ai
    ```

2. Run the game:
    ```bash
    python tic_tac_toe_ai.py
    ```

3. Follow the prompts to play against the AI!

---

## 🎯 Gameplay Instructions

- You play as `'X'`, and the AI plays as `'O'`.
- Input a number between **1 and 9** to place your move.
- Reference board shows positions:

```
  1 | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9
```

- The game ends when:
  - A player wins.
  - The board is full (tie).
- At the end, the number of explored states is displayed for performance insight.

---

## 🧪 AI Evaluation Heuristic

The heuristic function:
- Rewards lines (rows, columns, diagonals) where the AI can potentially win.
- Penalizes lines occupied by the opponent.
- Returns a score that estimates how favorable a board is to the AI player.

---

## 📌 Key Functions

| Function | Description |
|---------|-------------|
| `print_board()` | Displays the current state of the board. |
| `is_winner()` | Checks for a winning player. |
| `is_full()` | Checks if the board is full (tie). |
| `heuristic()` | Evaluates non-terminal board states. |
| `alpha_beta_pruning()` | Core AI logic with pruning and depth control. |
| `best_move()` | Selects the best move for AI using Alpha-Beta. |
| `take_input()` | Handles user input and updates board. |
| `main()` | Orchestrates the game loop. |

---

## 📊 Performance Metric

At the end of each game, the program displays:
```
Number of states explored: <count>
```
This helps understand how effective Alpha-Beta Pruning was in reducing the number of evaluations compared to a brute-force Minimax approach.

---

## 📚 References

- [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)
- [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

---

## 🤝 Contributing

Contributions are welcome! You can:
- Improve the heuristic.
- Add difficulty levels.
- Build a GUI version using Tkinter or Pygame.
- Add support for multiplayer or networked play.

---

## 🧾 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ✨ Author

Developed by [Your Name].  
Feel free to connect on [GitHub](https://github.com/muqniturrehman) or submit issues and PRs!

Enjoy playing — and may the smartest player win! 🤖🎮
