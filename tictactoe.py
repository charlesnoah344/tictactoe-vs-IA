"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #nombre de coups déja joué = nombre de cases non EMPTY
    count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                count += 1

    if count % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            if col == EMPTY:
                moves.add((i, j))

    return moves
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # l'action doit etre dans actions(board) sinon Exeption
    if action not in actions(board):
        raise RuntimeError("action non valide")

    #copie profonde
    new_board = copy.deepcopy(board)
    
    #application du move au board
    i,j = action
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #verification sur les lignes et les colonnes   
    for i in range(len(board)):
        row = board[i]
        if EMPTY not in row and len(set(row)) == 1:
            if X in row:
                return X
            elif O in row:
                return O
        column = [board[j][i] for j in range(len(board))]
        if EMPTY not in column and len(set(column)) == 1:
            if X in column:
                return X
            elif O in column:
                return O

    #verification sur les diagonales
    diag1 = [board[i][i] for i in range(len(board))]
    diag2 = [board[i][2-i] for i in range(len(board))]

    if (EMPTY not in diag1 and len(set(diag1)) == 1) :
        if X in diag1:
                return X
        elif O in diag1:
                return O
        
    if (EMPTY not in diag2 and len(set(diag2)) == 1) :
        if X in diag2:
                return X
        elif O in diag2:
                return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #si on a trouvé un gagnant
    if winner is not None:
        return True 
    else:
        table = []
        for row in board:
            for col in row:
                table.append(col)
        
        #Si on a encore une case vide dans le tableau, la partie est en cours
        if True in any(table == EMPTY):
            return False
        #S'il n'ya plus de case vide alors la partie est finie 
        else:
            return True
         


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
