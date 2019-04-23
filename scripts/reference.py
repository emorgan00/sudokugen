import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../solver'))
from solver import *
from grid import grid_from_string

puzzle = grid_from_string('''

. . .   . . .   . . .
. . .   1 2 3   4 5 6
. . .   . . .   . . .

. . .   2 . .   . . .
. . .   3 . .   . . .
. . .   4 . .   . . .

. . .   5 . .   . . .
. . .   6 . .   . . .
. . .   7 . .   . . .

''')

print score(puzzle, 'KNIGHT', True)