import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

# 5.2.......17....................9......84.9...79..56..79.15.3.8..8.9.........8.19

puzzle = grid_from_string('''

5.2.......17......9.............9......84.9...79..56..79.15.3.8..8.9.........8.19

''')

if __name__ == '__main__':
	print score(puzzle, 'KNIGHT', True)