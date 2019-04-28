import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

093004560060003140004608309981345000347286951652070483406002890000400010029800034

''')

if __name__ == '__main__':
	print score(puzzle, 'CLASSIC', True)