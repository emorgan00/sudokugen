import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from solver import score
from grid import grid_from_string

puzzle = grid_from_string('''

. . . . . 6 . . .
. . 3 . . . . . 7
2 . . 3 . . 4 9 .
6 . . . . . . 4 5
. . 2 . . . 8 . .
. . . 1 . . . . .
3 . . . . . . . .
7 . . . . 1 . . 9
. . . . . . 5 . .

''')

print score(puzzle, 'KNIGHT', True)