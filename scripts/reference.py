import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

8 . 9 . . 4 . . .
. . . . 2 . . 8 3
. . 4 . . . . 9 .
. 8 . . . . . . .
. . . 2 7 . . . 8
. . . . . 1 . . .
. . . . . . . . .
. . . . . . 3 1 .
3 . . 5 1 . . . 6

''', 'CLASSIC')

if __name__ == '__main__':
	print score(puzzle, 'knight', True)