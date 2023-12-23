from constant import *
import copy
import cell
import random

def dead_state(width : int = WIDTH, height : int = HEIGHT) -> list:
    '''
    Returns an empty 2D array with all values
    initialized to 0 (dead cell)
    '''

    return [[0] * WIDTH for _ in range(HEIGHT)]

def random_state(width : int = WIDTH, height : int = HEIGHT) -> list:
    '''
    Returns a 2d array with all values
    randomly initialized to 1 or 0
    '''
    board = dead_state()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if random.random() >= 0.5:
                board[i][j] = 1

    return board

def next_state(board: list) -> list:
    '''
    Return the next state of the board given the current state
    generate as per the rules of the game of life
    '''
    new_board = copy.deepcopy(board)

    for i in range(len(board)):
        for j in range(len(board[i])):
           new_board[i][j] = cell.next_state(i, j, board)

    return new_board

def add_pattern(pattern : list, board : list) -> list:
    '''
    pattern is an array of dimensions <= board
    add pattern to the current (preferably empty) board
    '''
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            board[i][j] = pattern[i][j]

    return board
