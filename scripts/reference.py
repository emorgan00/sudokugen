import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from solver import *
from grid import grid_from_string

puzzle = grid_from_string('''

. . . . 9 6 1 . .
. 1 . 7 . 4 . . .
. . 6 . . . 2 8 .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. 6 1 . . . 7 . .
. . . 1 . 2 . 4 .
. . 3 9 7 . . . .

''')

print score(puzzle, 'KNIGHT', True)