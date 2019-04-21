import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from solver import *

puzzle = grid_from_string('''

. . . 6 . 1 . . .
. . . . 4 . . . .
. . . 2 8 3 . . .
6 . . . . . . . 1
2 . . . . . . . 7
. . . . . . . . .
. . . . 5 . . . .
. . . . 6 . . . .
. 3 7 . . . 5 2 .

''')

print score(puzzle, 'KNIGHT', True)