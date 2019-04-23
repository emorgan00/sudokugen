import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from grid import *
from itertools import product

def make_step(g, opts):
	'''try each method in turn, exiting once any progress is made and returning the difficulty score of that method
	return -1 if nothing works'''

# ELIMINATE BY DIRECT CONFLICT (this method has a score of 0, and thus does not early-exit)

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] != -1:
			k = g[x][y]
			for i, j in neighbors_all(x, y, 'KNIGHT'): # from grid module
				if k in opts[i][j]:
					opts[i][j].remove(k)

# COLLAPSE (collapse a list of opts w/ len 1 into a grid number) (score: 1)

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] != -1: continue
		if len(opts[x][y]) == 0:
			raise Exception("No solution at "+str(x)+", "+str(y))
		if len(opts[x][y]) == 1:
			g[x][y] = opts[x][y].pop()
			return 1, 'COLLAPSE'

# BOX/ROW/COL SLICE (score: 1)

	def slice_group(group):
		count = [[0, 0, 0] for _ in xrange(9)]
		for x, y in group:
			if g[x][y] != -1: continue
			for k in opts[x][y]:
				count[k][0] += 1
				count[k][1] = x
				count[k][2] = y
		for k, c in enumerate(count):
			if c[0] == 1:
				g[c[1]][c[2]] = k
				return True

	# boxes
	for cx, cy in product(xrange(0, 9, 3), xrange(0, 9, 3)):
		if slice_group(product(xrange(cx, cx+3), xrange(cy, cy+3))): return 1, 'BOX SLICE'

	# rows/cols
	for i in xrange(9):
		if slice_group(product([i], xrange(9))): return 1, 'ROW SLICE'
		if slice_group(product(xrange(9), [i])): return 1, 'COL SLICE'

# at this point, we will need to start using pairs, which are set up here
# pair format: (k, [(x, y), (x, y)]) (same goes for triples, quads)
	
	pairs = []
	def add_pairs_in_group(group):
		count = [[] for _ in xrange(9)]
		for x, y in group:
			if g[x][y] != -1: continue
			for k in opts[x][y]:
				count[k].append((x, y))
		
		for k in xrange(9):
			if len(count[k]) != 2: continue
			pairs.append((k, count[k]))

	# boxes
	for cx, cy in product(xrange(0, 9, 3), xrange(0, 9, 3)):
		add_pairs_in_group(product(xrange(cx, cx+3), xrange(cy, cy+3)))

	# rows/cols
	for i in xrange(9):
		add_pairs_in_group(product([i], xrange(9)))
		add_pairs_in_group(product(xrange(9), [i]))

# LINEAR PAIR SLICE (score: 5)

	for pair in pairs:
		print pair

# NOTHING WORKED (either we are done, or the puzzle is unsolvable)

	return -1, 'DONE'

def knight_score(g, verbose = False):
	'''generate a score on how advanced techniques are needed to solve'''
	score = 0
	opts = [[range(9) if g[x][y] == -1 else [] for y in xrange(9)] for x in xrange(9)]

	if verbose:
		print 'STARTING POSITION 0'
		print_grid(g)

	while True:
		s, name = make_step(g, opts)
		if s == -1: break

		score += s
		if verbose:
			print name+' '+str(score)
			print_grid(g)

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] == -1: return -1

	return score