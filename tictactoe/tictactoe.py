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
    count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                count += 1
    
    if count%2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                ans.add((i,j))
    return ans



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    b = copy.deepcopy(board)
    i,j = action
    if b[i][j] != EMPTY or i not in range(0,3) or j not in range(0,3):
        raise RuntimeError("incompatible")
    else:
        b[i][j] = player(b)
    
    return b



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    hor_X = board.count([X,X,X])
    hor_O = board.count([O,O,O])
    t = [[row[i] for row in board] for i in range(3)]
    ver_X = t.count([X,X,X])
    ver_O = t.count([O,O,O])

    d = [board[i][i] for i in range(3)]
    anti_d = [board[i][2-i] for i in range(3)]

    if hor_X != 0 or ver_X != 0 or d.count(X) == 3 or anti_d.count(X) == 3:
        return X 
    elif hor_O != 0 or ver_O != 0 or d.count(O) == 3 or anti_d.count(O) == 3:
        return O 
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    if any(EMPTY in row for row in board):
        return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax_helper(board):
    if terminal(board):
        return (utility(board), None)

    ans = None
    num = None
    if player(board) == X:
        num = -100
        for a in actions(board):
            val = minimax_helper(result(board,a))[0]
            if val > num:
                num = val
                ans = a
            
    
    else:
        num = 100
        for a in actions(board):
            val = minimax_helper(result(board,a))[0]
            if val < num:
                num = val
                ans = a

    return (num,ans)

    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    return minimax_helper(board)[1]

