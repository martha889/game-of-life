import render
import pattern
from constant import *

# height, width
DIFFERENCE = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]

def check_neighbours(i: int, j: int, board: list) -> int:
    '''
    return the number of alive neighbours of the current cell
    '''
    neighbours = 0

    for diff in DIFFERENCE:
        row = i + diff[0]
        col = j + diff[1]

        if 0 <= row < len(board[0]) and 0 <= col < len(board) and board[row][col]:
            neighbours += 1

    return neighbours

def next_state(i: int, j: int, board: list) -> int:
    '''
    return the next state of the given cell
    '''

    live_neighbours = check_neighbours(i, j, board)
    ret = 0

    if board[i][j]:
        # cell is alive
        if live_neighbours == 2 or live_neighbours == 3:
            ret = 1
    else:
        if live_neighbours == 3:
            ret = 1

    return ret
