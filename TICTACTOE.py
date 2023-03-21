import random

def print_board(board):
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

def player_move(board, player):
    position = int(input("Pick a position from 0 to 8:"))
    if position >= 0 and position <= 8 and board[position] == '_':
        board[position] = player
    else:
        print("That's not a valid location")

def computer_move(board):
    position = random.randint(0, 8)
    while board[position] != '_':
        position = random.randint(0, 8)
    board[position] = 'O'

def winner(board):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for pos in winning_positions:
        if all(board[p] == 'X' for p in pos):
            return 'X'
        elif all(board[p] == 'O' for p in pos):
            return 'O'
    if '_' not in board:
        return 'Tie'
    return None

def play_game():
    board = ['_' for _ in range(9)]
    print("Ready to play Tic Tac Toe!")
    print_board(board)
    player = 'X'
    while True:
        if player == 'X':
            player_move(board, player)
        else:
            computer_move(board)
        print_board(board)
        result = winner(board)
        if result is not None:
            if result == 'Tie':
                print("It's a tie!")
            else:
                print(f"{result} won!")
            break
        player = 'X' if player == 'O' else 'O'

play_game()
