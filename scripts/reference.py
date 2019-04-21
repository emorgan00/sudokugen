import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from solver import *

puzzle = grid_from_string('''

. . 3   5 6 7   8 9 4
. . .   . . .   . . .
. . 8   . . .   . . .

. . 4   . . .   . . .
. . 5   . . .   . . .
. . 6   . . .   . . .

. . 7   . . .   . . .
. . .   . . .   . . .
. . .   . . .   . . .

''')

print score(puzzle, 'DEFAULT', True)