import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

720408030080000047401076802810739000000851000000264080209680413340000008168943275

''')

if __name__ == '__main__':
	print score(puzzle, 'CLASSIC', True)