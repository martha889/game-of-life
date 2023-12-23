from colorama import Style
from constant import LIVE_COLOR, DEAD_COLOR

def reset_screen():
    print(Style.RESET_ALL)

def render(board: list) -> None:
    '''
    Pretty print the given board
    '''

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                print(LIVE_COLOR + "*", end='  ')
            else:
                print(DEAD_COLOR + '.', end='  ')
        print()
