import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from generator import *

# generate many puzzles, and keep track of the best ones. also, write them to a file.

m_score = -1
m_clues = 81

puzzles = []

file_out = 'freeform.txt'

for _ in xrange(100):
	g = generate_grid('KNIGHT')
	s = score(g, 'KNIGHT')
	c = sum(sum(x != -1 for x in row) for row in g)
	puzzles.append((g, s, c))

with open(file_out, 'w') as f:
	puzzles.sort(key = lambda x: (x[1], x[2]), reverse = True)
	f.write('HARDEST:')
	for p, s, c in puzzles:
		f.write('\n\nSCORE: '+str(s)+'\n')
		f.write('CLUES: '+str(c)+'\n')
		f.write(grid_to_string(p))

	puzzles.sort(key = lambda x: (x[2], x[1]))
	f.write('\n\nFEWEST CLUES:')
	for p, s, c in puzzles:
		f.write('\n\nSCORE: '+str(s)+'\n')
		f.write('CLUES: '+str(c)+'\n')
		f.write(grid_to_string(p))