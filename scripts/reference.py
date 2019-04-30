import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

......5..3.1...9..5.7...16.4............5............8.35...7.9..6...8.1..9......

''')

if __name__ == '__main__':
	print score(puzzle, 'KNIGHT', True)