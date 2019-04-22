import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from solver import *

puzzle = grid_from_string('''

2 . . 3 . 8 . . .
. . . . . . . . .
. . . . . . 3 . 2
. . . . . 4 . 9 .
. . 6 . . . . 1 .
. . 1 . . 9 . . .
. 1 2 . . . . . .
. . 5 8 7 . . . .
6 . . . . . . . .

''')

print score(puzzle, 'KNIGHT', True)