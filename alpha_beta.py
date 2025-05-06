import math
count = 0

# Initialize a 3x3 Tic-Tac-Toe board with empty spaces.
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    """Prints current state of the board."""
    print("\nCurrent Board:")
    for i in range(len(board)):
        print(f"  {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i == 0 or i == 1:
            print(" -----------")

def is_winner(board, player):
    """Checks if the given player ('X' or 'O') has won the game."""
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    """Checks if the board is full."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def heuristic(board, player):
    """Returns a heuristic score evaluating the board favoring the given player."""
    score = 0
    opponent = 'O' if player == 'X' else 'X'

    for x in range(3):
        if not (board[x][0] == opponent or board[x][1] == opponent or board[x][2] == opponent):
            score += 1

    for y in range(3):
        if not (board[0][y] == opponent or board[1][y] == opponent or board[2][y] == opponent):
            score += 1

    if not (board[0][0] == opponent or board[1][1] == opponent or board[2][2] == opponent):
        score += 1

    if not (board[0][2] == opponent or board[1][1] == opponent or board[2][0] == opponent):
        score += 1

    return score

def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    global count
    count += 1

    if is_winner(board, 'O'):
        return math.inf
    if is_winner(board, 'X'):
        return -math.inf
    if is_full(board):
        return 0
    if depth == 0:
        max_score = heuristic(board, 'O')
        min_score = heuristic(board, 'X')
        return min_score - max_score

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    score = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    score = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def best_move():
    """Finds and executes the best move for AI ('O') using the Alpha-Beta Pruning function with limited depth."""
    best_score = -math.inf
    move = None

    depth_limit = 3  # <<<----- Depth limit retained

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                score = alpha_beta_pruning(board, depth_limit, -math.inf, math.inf, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    if move:
        board[move[0]][move[1]] = 'O'

def refrence():
    """Displays reference board positions to help the user choose a move."""
    print("Reference Board:")
    reference_board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    print_board(reference_board)

def take_input():
    """Takes user input (1-9), validates it, and marks 'X' on the board."""
    while True:
        try:
            number = int(input("Enter move (1-9): "))
            if number < 1 or number > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            row = (number - 1) // 3
            col = (number - 1) % 3

            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def main():
    global count
    refrence()
    print("==========================")

    while True:
        print_board(board)

        take_input()
        if is_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win! 🎉")
            print(f"Number of states explored: {count}")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            print(f"Number of states explored: {count}")
            break

        best_move()
        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins! Better luck next time. 🤖")
            print(f"Number of states explored: {count}")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            print(f"Number of states explored: {count}")
            break

main()
