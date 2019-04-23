from sys import stdout
from grid import *
from itertools import product

def make_step(g, opts):
	'''try each method in turn, exiting once any progress is made and returning the difficulty score of that method
	returns (score, name of method, grid modified?)'''

# ELIMINATE BY DIRECT CONFLICT (this method has a score of 0, and thus does not early-exit)

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] != -1:
			k = g[x][y]
			for i, j in neighbors_all(x, y, 'KNIGHT'): # from grid module
				if k in opts[i][j]:
					opts[i][j].remove(k)

# COLLAPSE (score: 1)
# collapse a list of opts w/ len 1 into a grid number

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] != -1: continue
		if len(opts[x][y]) == 0:
			return -1, 'ERROR', False
		if len(opts[x][y]) == 1:
			g[x][y] = opts[x][y].pop()
			return 1, 'COLLAPSE', True

# BOX/ROW/COL SLICE (score: 1)
# if an option only appears once in a group, assign that grid square that value

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
		if slice_group(product(xrange(cx, cx+3), xrange(cy, cy+3))): return 1, 'BOX SLICE', True

	# rows/cols
	for i in xrange(9):
		if slice_group(product([i], xrange(9))): return 1, 'ROW SLICE', True
		if slice_group(product(xrange(9), [i])): return 1, 'COL SLICE', True

# at this point, we will need to start using pairs, which are set up here
# pair format: (k, [(x, y), (x, y)]) (same goes for triples, quads)
	
	pairs = []
	triples = []
	def add_pairs_in_group(group):
		count = [[] for _ in xrange(9)]
		for x, y in group:
			if g[x][y] != -1: continue
			for k in opts[x][y]:
				count[k].append((x, y))
		
		for k in xrange(9):
			if len(count[k]) == 2:
				pairs.append((k, count[k]))
			if len(count[k]) == 3:
				triples.append((k, count[k]))

	# boxes
	for cx, cy in product(xrange(0, 9, 3), xrange(0, 9, 3)):
		add_pairs_in_group(product(xrange(cx, cx+3), xrange(cy, cy+3)))

	# rows/cols
	for i in xrange(9):
		add_pairs_in_group(product([i], xrange(9)))
		add_pairs_in_group(product(xrange(9), [i]))

# LINEAR/BOX PAIR SLICE (score: 10)
# take all pairs which are arranged along a line, and slice along that line and in that box

	def evaluate_pair(pair):
		e = False
		k = pair[0]
		ax, ay = pair[1][0]
		bx, by = pair[1][1]

		if ax == bx: # same x
			for i in xrange(9):
				if i != ay and i != by and k in opts[ax][i]:
					opts[ax][i].remove(k)
					e = True

		if ay == by: # same y
			for i in xrange(9):
				if i != ax and i != bx and k in opts[i][ay]:
					opts[i][ay].remove(k)
					e = True

		box = same_box(ax, ay, bx, by)
		if box:
			for i, j in product(xrange(box[0], box[0]+3), xrange(box[1], box[1]+3)):
				if (i != ax or j != ay) and (i != bx or j != by) and k in opts[i][j]:
					opts[i][j].remove(k)
					e = True
		return e

	edited = False
	for pair in pairs:
		if evaluate_pair(pair): edited = True

	if edited: return 10, 'PAIR SLICE', False

# LINEAR/BOX IMPLICIT PAIR SLICE (score: 10)
# an implicit pair exists which we can slice by

	implicit_pairs = []
	def implicit_pairs_in_group(group):
		candidates = []
		for x, y in group:
			if len(opts[x][y]) == 2: candidates.append((x, y))

		for i in xrange(len(candidates)):
			for j in xrange(i):
				ax, ay = candidates[i]
				bx, by = candidates[j]

				k0, k1 = opts[ax][ay]
				if k0 == opts[bx][by][0] and k1 == opts[bx][by][1]:
					implicit_pairs.append((k0, [candidates[i], candidates[j]]))
					implicit_pairs.append((k1, [candidates[i], candidates[j]]))

	# boxes
	for cx, cy in product(xrange(0, 9, 3), xrange(0, 9, 3)):
		implicit_pairs_in_group(product(xrange(cx, cx+3), xrange(cy, cy+3)))

	# rows/cols
	for i in xrange(9):
		implicit_pairs_in_group(product([i], xrange(9)))
		implicit_pairs_in_group(product(xrange(9), [i]))

	for pair in implicit_pairs:
		if evaluate_pair(pair): edited = True
		pairs.append(pair)

	if edited: return 10, 'IMPLICIT PAIR SLICE', False

# KNIGHT PAIR SLICE (score: 100)
# if both parts of a pair see the same tile by knight moves, we can eliminate
# as a side note, reaching this point is rare enough that we don't need to worry about runtimes of these tactics

	def intersecting(a, b):
		ax, ay = a
		bx, by = b
		if ax == bx and ay == by: return False # same tile
		if ax == bx or ay == by or same_box(ax, ay, bx, by): return True
		if (ax-bx, ay-by) in [(2, 1), (-2, 1), (1, 2), (-1, 2), (2, -1), (-2, -1), (1, -2), (-1, -2)]: return True
		return False

	def common_tiles(pair):
		a, b = pair[1]
		out = []
		for p in product(xrange(9), xrange(9)):
			if intersecting(p, a) and intersecting(p, b):
				out.append(p)
		return out

	def evaluate_pair_knight(pair):
		k = pair[0]
		e = False
		for x, y in common_tiles(pair):
			if k in opts[x][y]:
				opts[x][y].remove(k)
				e = True
		return e

	edited = False
	for pair in pairs:
		if evaluate_pair_knight(pair): edited = True

	if edited:
		return 100, 'KNIGHT PAIR SLICE', False

# NOTHING WORKED (either we are done, or the puzzle is unsolvable)

	return -1, 'DONE', True

def knight_score(g, verbose = False):
	'''generate a score on how advanced techniques are needed to solve'''

	score = 0
	opts = [[range(9) if g[x][y] == -1 else [] for y in xrange(9)] for x in xrange(9)]

	if verbose:
		print 'STARTING POSITION 0'
		print_grid(g)

	while True:
		s, name, display = make_step(g, opts)
		if s == -1: break

		score += s
		if verbose:
			print name+' '+str(score)
			if display:
				print_grid(g)
			stdout.flush()

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] == -1: return -1

	return score