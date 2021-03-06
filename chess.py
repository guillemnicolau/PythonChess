import argparse
import logging
from tkinter import Tk
from src.conf.settings import size_x, size_y
from src.board import Board
from src.conf.logger import setup_logger
from src.game_execution import GameExecution


formatter = logging.Formatter('%(message)s')
current_logger = setup_logger('log1', "logs/current.log", with_formatter=formatter)
super_logger = setup_logger('log2', "logs/all.log")


if __name__ == "__main__":

    # Arguments are taken from command line

    parser = argparse.ArgumentParser(description='Python Chess',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', action="store_true",
                        help="Activate learning mode mode",
                        default=False, dest='learn')
    args = parser.parse_args()
    if args.learn:
        mode = 'learn'
    else:
        mode = 'normal'

    root = Tk()
    board = Board(size_x, size_y)
    app = GameExecution(mode, board)
    app.show_board()
    root.mainloop()
