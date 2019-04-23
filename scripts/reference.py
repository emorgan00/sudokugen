import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from solver import score
from grid import grid_from_string

puzzle = grid_from_string('''

. . . . 6 1 7 . .
7 . 5 . 3 . . 2 .
. . . . . . 9 . .
. . . . . . . . .
1 . . . 8 . . . 9
. . . . . . . . .
. . 2 . . . . . .
. 4 . . 7 . 3 . 2
. . 3 5 9 . . . .

''')

print score(puzzle, 'KNIGHT', True)