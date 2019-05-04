import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

000000000001900500560310090100600028004000700270004003040068035002005900000000000

''', 'CLASSIC')

if __name__ == '__main__':
	print score(puzzle, 'classic', True)