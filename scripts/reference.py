import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

. . . . . . . . .
. 4 3 6 . . . 1 .
. . . 3 . . 6 . .
. . 1 . . 6 . . .
. 5 . . 2 . . 8 .
. . . 8 . . 7 . .
. . 8 ? . 3 . . .
. 9 . . . 8 3 5 .
. . . . . . . . .

''')

if __name__ == '__main__':
	print score(puzzle, 'KNIGHT', True)