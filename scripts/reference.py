import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

puzzle = grid_from_string('''

...3................61.......1...6.8..7....1.6.........4....1....3....67........53TB22R27KVT53DIDB0

''', 'BETWEEN')

if __name__ == '__main__':
	print score(puzzle, 'BETWEEN', True)