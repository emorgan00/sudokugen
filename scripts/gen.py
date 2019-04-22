import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from generator import *

# generate many puzzles, and keep track of the best ones. also, write them to a file.

m_score = -1
m_clues = 81

puzzles = []

for _ in xrange(3):
	g = generate_symmetric_grid('R', 'KNIGHT')
	s = score(g, 'KNIGHT')
	c = sum(sum(x != -1 for x in row) for row in g)
	puzzles.append((g, s, c))

with open('puzzles.txt', 'w') as f:
	puzzles.sort(key = lambda x: x[1], reverse = True)
	f.write('HARDEST:\n')
	for p, s, c in puzzles:
		f.write('SCORE: '+str(s))
		f.write('CLUES: '+str(c))
		f.write(grid_to_string(p))

	puzzles.sort(key = lambda x: x[2])
	f.write('FEWEST CLUES:\n')
	for p, s, c in puzzles:
		f.write('SCORE: '+str(s))
		f.write('CLUES: '+str(c))
		f.write(grid_to_string(p))
