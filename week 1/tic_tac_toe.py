
import math

# Game board
board = [" " for _ in range(9)]

# Score tracking
stats = {"Player": 0, "AI": 0, "Draw": 0}

def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")
    print()

def is_winner(player):
    win_patterns = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if is_winner("O"):
        return 1
    if is_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_move():
    while True:
        try:
            move = int(input("Choose position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Position occupied!")
        except:
            print("Invalid input!")

def play_game():
    global board
    board = [" " for _ in range(9)]
    print_board()

    while True:
        player_move()
        print_board()

        if is_winner("X"):
            print("You win!")
            stats["Player"] += 1
            break

        if is_draw():
            print("Draw!")
            stats["Draw"] += 1
            break

        ai_move()
        print("AI's move:")
        print_board()

        if is_winner("O"):
            print("AI wins!")
            stats["AI"] += 1
            break

def main():
    while True:
        play_game()
        print("\nScoreboard:")
        print(stats)

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            break

main()
