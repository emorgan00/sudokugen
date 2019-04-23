import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from solver import score
from grid import grid_from_string

puzzle = grid_from_string('''

. . . 1 2 6 . . .
. . . . 5 . . . .
6 . . 9 4 . . . 8
. . . . . . 2 . .
. . . . . . . . .
. . 6 . . . . . .
3 . . . 1 4 . . 2
. . . . 3 . . . .
. . . 8 6 2 . . .

''')

print score(puzzle, 'KNIGHT', True)