import math
import random

def print_board(board):
    print()
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---+---+---")
    print()

def available_moves(board):
    return [i for i, v in enumerate(board) if v == " "]

def check_winner(board):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  # lignes
        (0,3,6),(1,4,7),(2,5,8),  # colonnes
        (0,4,8),(2,4,6)           # diagonales
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Tie"
    return None

def player_move(board, symbol):
    while True:
        choice = input(f"Joueur {symbol}, choisis une case (1-9) : ")
        try:
            pos = int(choice) - 1
            if pos not in range(9):
                print("⛔ Tape un chiffre entre 1 et 9.")
                continue
            if board[pos] != " ":
                print("⛔ Case occupée !")
                continue
            board[pos] = symbol
            break
        except:
            print("⛔ Entrée invalide.")

def minimax(board, depth, is_max, ai, human):
    winner = check_winner(board)
    if winner == ai:
        return 10 - depth
    if winner == human:
        return depth - 10
    if winner == "Tie":
        return 0

    if is_max:
        best = -math.inf
        for m in available_moves(board):
            board[m] = ai
            score = minimax(board, depth + 1, False, ai, human)
            board[m] = " "
            best = max(best, score)
        return best
    else:
        best = math.inf
        for m in available_moves(board):
            board[m] = human
            score = minimax(board, depth + 1, True, ai, human)
            board[m] = " "
            best = min(best, score)
        return best

def ai_move(board, ai, human):
    # Premier coup rapide
    if len(available_moves(board)) == 9:
        return random.choice([0, 2, 4, 6, 8])

    best_score = -math.inf
    best_move = None

    for m in available_moves(board):
        board[m] = ai
        score = minimax(board, 0, False, ai, human)
        board[m] = " "
        if score > best_score:
            best_score = score
            best_move = m

    return best_move

def game():
    board = [" "] * 9
    human = "X"
    ai = "O"
    turn = "human"

    print("===== JEU : TIC TAC TOE (X-O) =====")

    while True:
        print_board(board)

        if turn == "human":
            player_move(board, human)
            turn = "ai"

        else:
            print("🤖 L’IA réfléchit...")
            m = ai_move(board, ai, human)
            board[m] = ai
            turn = "human"

        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Tie":
                print("⚪ Match nul !")
            else:
                print("🏆 Le gagnant est :", result)
            break

# Lancer le jeu
game()
