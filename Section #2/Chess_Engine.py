 ###########################################
##=========================================##
## CHESS ENGINE.py                         ##
##-----------------------------------------##
# Runs alone using bit-string complexities.##
##-----------------------------------------##
##       >Created: 20/14/2025<             ##
##=========================================##
 ###########################################

# STEP 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print('''Step 1:
Install python-chess''')

print("pip install python-chess")

print("If possible, that is")

# STEP 2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print('''Step 2:
Basic Minimax Engine with Alpha-Beta''')
####CODE BELOW####

import chess
import chess.engine
import random

# Simple piece value evaluation
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0
}

def evaluate_board(board):
    """Static evaluation: material count"""
    if board.is_checkmate():
        return -9999 if board.turn else 9999
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0

    eval = 0
    for piece_type in PIECE_VALUES:
        eval += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        eval -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]
    return eval

def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if is_maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def choose_best_move(board, depth=3):
    _, move = minimax(board, depth, -float('inf'), float('inf'), board.turn)
    return move

# Play vs engine
def play_game():
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = choose_best_move(board, depth=3)
        else:
            move = random.choice(list(board.legal_moves))  # simulate weak opponent
        print(f"\n{board.san(move)}\n")
        board.push(move)
    print(board)
    print("Game Over:", board.result())

play_game()

####END CODE####
