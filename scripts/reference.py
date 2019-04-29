import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

. . . . . . . 8 .
. . . . . . . . .
9 8 7 . . . . . .
. . . 2 . 3 7 . .
2 . . . . . . . .
. . . . . 6 . . .
. . . . . 1 2 . .
. . . . . . . . .
. . . . 4 . 9 . 1

''')

if __name__ == '__main__':
	print score(puzzle, 'KNIGHT', True)