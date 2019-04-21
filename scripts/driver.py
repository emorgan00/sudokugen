import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from solver import *

# this will generate 1000 puzzles and print the hardest ones along with their respective scores

m = 100
for _ in xrange(1000):
	puzzle = grid('KNIGHT')
	puzzle = partial_grid(puzzle, 0.3)
	old = [[x for x in row] for row in puzzle]

	s = score(puzzle, 'KNIGHT')
	if s > m:
		m = s
		print s
		print_grid(old)