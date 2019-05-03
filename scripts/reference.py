import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

..9...7.2...9....5.5..4.....1.......7.......1.......9.....6..3.3....9...5.8...6..

''', 'CLASSIC')

if __name__ == '__main__':
	print score(puzzle, 'knight', True)