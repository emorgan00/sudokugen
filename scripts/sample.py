import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *
from app import compress

if __name__ == '__main__':

	variant = 'BETWEEN'

	# puzzle = generate_symmetric_grid('R', 'CLASSIC', None, True)
	puzzle = generate_grid(variant, 4.0, True)
	print score(puzzle, variant)
	print_grid(puzzle, variant, True)