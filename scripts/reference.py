import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

....5.26....2.....2...765...........7...9...6...........142...5.....3....25.1....

''')

if __name__ == '__main__':
	print score(puzzle, 'KNIGHT', True)