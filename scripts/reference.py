import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

3 . . . 1 7 2 4 .
. . 5 . . . . . .
. . . . . 8 . . .
9 8 6 . 5 . . . .
1 . . . . 2 . . .
. . . . . . . . .
. . . . . 1 . . 4
. . 4 3 . . . . .
. 7 . . 6 . . . .

''')

if __name__ == '__main__':
	print score(puzzle, 'KNIGHT', True)