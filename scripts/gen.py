import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from sudoku import *

# generate many puzzles, and keep track of the best ones. also, write them to a file.

m_score = -1
m_clues = 81

puzzles = []

file_out = 'rsymmetry.txt'

if __name__ == '__main__':
	for i in xrange(1, 101):
		g = generate_symmetric_grid('R', 'KNIGHT')
		s = score(g, 'KNIGHT')
		c = sum(sum(x != -1 for x in row) for row in g)
		puzzles.append((g, s, c))
		print str(i)+' / 100'
		sys.stdout.flush()

	with open(file_out, 'w') as f:
		puzzles.sort(key = lambda x: (x[1], x[2]), reverse = True)
		f.write('HARDEST 5:')
		for p, s, c in puzzles[:5]:
			f.write('\n\nSCORE: '+str(s)+'\n')
			f.write('CLUES: '+str(c)+'\n')
			f.write(grid_to_string(p))

		puzzles.sort(key = lambda x: (x[2], x[1]))
		f.write('\n\nFEWEST CLUES:')
		for p, s, c in puzzles:
			f.write('\n\nSCORE: '+str(s)+'\n')
			f.write('CLUES: '+str(c)+'\n')
			f.write(grid_to_string(p))