import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from solver import *

puzzle = grid_from_string('''

. 6 5   . . .   2 3 4
. . .   . . .   . . .
. 3 4   . . .   5 6 .

. . .   . . .   . . .
. . 3   . . .   . . .
. . 2   . . .   . . .

. . .   . . .   . . .
. 1 .   . . .   . . .
. . .   . . .   . . 1

''')

print score(puzzle, 'DEFAULT', True)