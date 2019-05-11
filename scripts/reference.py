import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

........1...............................1........................................J7FJ4069Z5DK9C04E5

''', 'BETWEEN')

if __name__ == '__main__':
	print score(puzzle, 'BETWEEN', True)