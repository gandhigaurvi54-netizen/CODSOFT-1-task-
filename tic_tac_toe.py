import math


board = [' ' for _ in range(9)]


def print_board():
    print()
    for i in range(3):
        print(" " + board[i * 3] + " | " + board[i * 3 + 1] + " | " + board[i * 3 + 2])
        if i < 2:
            print("---|---|---")
    print()


def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False



def is_draw():
    return ' ' not in board



def available_moves():
    return [i for i in range(9) if board[i] == ' ']



def minimax(is_maximizing):

    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for move in available_moves():
            board[move] = 'O'
            score = minimax(False)
            board[move] = ' '
            best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for move in available_moves():
            board[move] = 'X'
            score = minimax(True)
            board[move] = ' '
            best_score = min(score, best_score)

        return best_score



def ai_move():
    best_score = -math.inf
    best_move = None

    for move in available_moves():
        board[move] = 'O'
        score = minimax(False)
        board[move] = ' '

        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = 'O'



def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move in available_moves():
                board[move] = 'X'
                break
            else:
                print("Invalid move! Try again.")

        except ValueError:
            print("Please enter a number.")



def play_game():

    print("TIC-TAC-TOE")
    print("You are X")
    print()

    print("Board positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:

        print_board()

        
        human_move()

        if check_winner('X'):
            print_board()
            print("You win!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

      
        print("AI is making a move...")
        ai_move()

        if check_winner('O'):
            print_board()
            print("AI wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break


# Start game
play_game()
