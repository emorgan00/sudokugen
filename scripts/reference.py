import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

variant = 'BETWEEN'
puzzle = grid_from_string('''

.....8........5......4......3..7.........3..........1........4.9.................SZ0RO38FK5RAFA8EBV

''', variant)

if __name__ == '__main__':
	print solve(puzzle, variant, True)
	print_grid(puzzle, variant, True)