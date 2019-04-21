import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from grid import *
from solver import *

m = 150 # a decent baseline score
for _ in xrange(1000):
	puzzle = grid('KNIGHT')
	puzzle = partial_grid(puzzle, 0.3)
	old = [[x for x in row] for row in puzzle]

	s = score(puzzle, 'KNIGHT')
	if s > m:
		m = s
		print s
		print_grid(old)