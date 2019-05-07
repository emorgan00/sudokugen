import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

.....13....4..67.95..47.1...65..7......9.....8......4..3..854....76..9....27....5


''', 'CLASSIC')

if __name__ == '__main__':
	print score(puzzle, 'classic', True)