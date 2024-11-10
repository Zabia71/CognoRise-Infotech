import math
def initialize_board():
    return [' ' for _ in range(9)]  

def display_board(board):
    print("\n")
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'Tie'  # Tie if no spaces are left
    return None

# Minimax algorithm
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':  # AI wins
        return 1
    elif winner == 'X':  # Player wins
        return -1
    elif winner == 'Tie':  # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

# AI's move
def ai_move(board):
    best_score = -math.inf
    move = None
    for possible_move in available_moves(board):
        board[possible_move] = 'O'
        score = minimax(board, False)
        board[possible_move] = ' '
        if score > best_score:
            best_score = score
            move = possible_move
    board[move] = 'O'
    print(f"AI chooses position {move + 1}")

# Player's move
def player_move(board):
    move = -1
    while move not in available_moves(board):
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in available_moves(board):
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
    board[move] = 'X'
    print(f"You chose position {move + 1}")

# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic Tac Toe! You are 'X' and the AI is 'O'.")
    display_board(board)

    while True:
        player_move(board)
        display_board(board)
        if check_winner(board) == 'X':
            print("Congratulations! You win!")
            break
            
        elif check_winner(board) == 'Tie':
            print("It's a tie!")
            break
        ai_move(board)
        display_board(board)
        if check_winner(board) == 'O':
            print("The AI wins. Better luck next time!")
            break
        elif check_winner(board) == 'Tie':
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
