import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

if __name__ == '__main__':
	# puzzle = generate_symmetric_grid('R', 'CLASSIC', None, True)
	puzzle = generate_grid('KNIGHT', None, True)
	print score(puzzle, 'KNIGHT')
	print_grid(puzzle)