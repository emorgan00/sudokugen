import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

.6....3.9...4..76.......2....925..4.............8.....3............6...274.1.....S7B704A90ZLA7Q00XA

''', 'BETWEEN')

if __name__ == '__main__':
	print score(puzzle, 'BETWEEN', True)