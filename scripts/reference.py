import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from solver import *

puzzle = grid_from_string('''

. . . . . 1 . . .
. . . 5 . . . . .
7 4 . . . . 2 8 .
. . 6 . . . . . .
. 1 . . . . . . .
. 7 . . . . . . .
. 9 . 4 . . . . .
1 . . 2 6 . . . .
4 . 7 . . 9 . . 3

''')

print score(puzzle, 'KNIGHT', True)