import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from solver import score
from grid import grid_from_string

puzzle = grid_from_string('''

. . . 6 . . . . 8
. . . . . . . . .
. . 8 . . . . 2 .
. 3 4 5 . . 2 . .
. . . . 7 . . . .
. . 6 . . 1 3 8 .
. 1 . . . . 7 . .
. . . . . . . . .
6 . . . . 2 . . .

''')

print score(puzzle, 'KNIGHT', True)