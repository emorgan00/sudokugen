import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

if __name__ == '__main__':
	puzzle = generate_symmetric_grid('R', 'KNIGHT', True)
	# puzzle = generate_grid('KNIGHT', True)
	print score(puzzle, 'KNIGHT')
	print_grid(puzzle)