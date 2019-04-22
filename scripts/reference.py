import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from solver import *
from grid import grid_from_string

puzzle = grid_from_string('''

9 . . . . . . 3 .
. . . 1 . 4 8 7 9
7 . . . . . . 2 .
. . 8 . . . . . .
3 . . . . 5 . . .
2 . . . . 1 . . .
4 . . . . . . . .
. . . . 6 . . . .
. . 3 . . . . 4 .

''')

print score(puzzle, 'KNIGHT', True)