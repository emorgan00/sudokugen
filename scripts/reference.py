import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from grid import *
from solver import *

puzzle = grid_from_string('''

7 4 5 . . . . 3 9
6 . . . . 9 . . .
. . . . . . . . .
9 . . . . . . 8 .
. . . . 8 . 9 1 .
. 8 . . . 4 . 7 6
. . . . . . 7 . .
4 . 1 . . 3 . 9 .
. . 7 . . . 3 . .

''')

print score(puzzle, 'KNIGHT', True)