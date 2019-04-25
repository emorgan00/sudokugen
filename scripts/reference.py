import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

3 . . . . . . 7 .
5 . . . . 4 . 9 .
4 . . 5 . . . . .
. . . . . . . . 7
. . . . . . . . .
. . 1 . . . . . .
8 7 9 . . . . 3 .
2 . . . . . . 8 .
. 5 . . . . . 2 .

''')

if __name__ == '__main__':
	print score(puzzle, 'KNIGHT', True)