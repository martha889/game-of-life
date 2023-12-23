import time
import pattern
import board_generator
import render
import os


def main():
    board = board_generator.dead_state()
    board_generator.add_pattern(pattern.GOSPER_GLIDER_GUN, board)
    # board = board_generator.random_state()
    while True:
        os.system('clear')
        render.render(board)
        board = board_generator.next_state(board)
        time.sleep(0.2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        render.reset_screen()
    
