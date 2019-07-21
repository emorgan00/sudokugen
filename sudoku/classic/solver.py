from sys import stdout
from itertools import product
from grid import neighbors_all, same_box, in_range, grid_to_string

def make_step(g, opts):
	'''try each method in turn, exiting once any progress is made and returning the difficulty score of that method
	returns (score, name of method, grid modified?)'''

# ELIMINATE BY DIRECT CONFLICT (this method has a score of 0, and thus does not early-exit)

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] != -1:
			k = g[x][y]
			for i, j in neighbors_all(x, y): # from grid module
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

# SLICE (score: 1)
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
				opts[c[1]][c[2]] = []
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

# PAIR SLICE (score: 10)
# take all pairs which are arranged along a line, and slice along that line and in that box

	def evaluate_pair(pair): # this is the same as evaluate_pair_knight, but cheaper and doesn't include knight moves
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

# TRIPLE SLICE (score: 15)

	def evaluate_triple(triple):
		e = False
		k = triple[0]
		ax, ay = triple[1][0]
		bx, by = triple[1][1]
		cx, cy = triple[1][2]

		if ax == bx == cx: # same x
			for i in xrange(9):
				if i != ay and i != by and i != cy and k in opts[ax][i]:
					opts[ax][i].remove(k)
					e = True

		if ay == by == cy: # same y
			for i in xrange(9):
				if i != ax and i != bx and i != cx and k in opts[i][ay]:
					opts[i][ay].remove(k)
					e = True

		box = same_box(ax, ay, bx, by)
		test = same_box(ax, ay, cx, cy)
		if box and test:
			for i, j in product(xrange(box[0], box[0]+3), xrange(box[1], box[1]+3)):
				if (i != ax or j != ay) and (i != bx or j != by) and (i != cx or j != cy) and k in opts[i][j]:
					opts[i][j].remove(k)
					e = True
		return e

	edited = False
	for triple in triples:
		if evaluate_triple(triple): edited = True

	if edited: return 15, 'TRIPLE SLICE', False

# NAKED PAIR (score: 20)
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

	if edited: return 20, 'NAKED PAIR', False

# at this point, we may have some duplicate pairs, which we prune off here.

	distinct_pairs = []
	def same_pair(a, b):
		return a[0] == b[0] and a[1][0] == b[1][0] and a[1][1] == b[1][1]

	for pair in pairs:
		pair[1].sort()
		if all(not same_pair(pair, comp) for comp in distinct_pairs):
			distinct_pairs.append(pair)

	pairs = distinct_pairs

# OVERLAPPING PAIR (score: 25)

	for i in xrange(len(pairs)):
		a = pairs[i]
		for j in xrange(i):
			b = pairs[j]
			k0, k1 = a[0], b[0]
			if all(a[1][p] == b[1][p] for p in xrange(2)):
				for p in xrange(2):
					o = opts[a[1][p][0]][a[1][p][1]] 
					for k in xrange(9):
						if k != k0 and k != k1 and k in o:
							edited = True
							o.remove(k)

	if edited: return 25, 'OVERLAPPING PAIR', False

# OVERLAPPING TRIPLE (score: 30)
# note: this won't detect triples with pairs as components (which is most triples)
# note: this is currently commented out because it is SUPER expensive and rarely is useful

	# for i in xrange(len(triples)):
	# 	a = triples[i]
	# 	a[1].sort()
	# 	for j in xrange(i):
	# 		b = triples[j]
	# 		for h in xrange(j):
	# 			c = triples[h]
	# 			k0, k1, k2 = a[0], b[0], c[0]
	# 			if all(a[1][p] == b[1][p] == c[1][p] for p in xrange(3)):
	# 				for p in xrange(3):
	# 					o = opts[a[1][p][0]][a[1][p][1]] 
	# 					for k in xrange(9):
	# 						if k != k0 and k != k1 and k != k2 and k in o:
	# 							edited = True
	# 							o.remove(k)

	# if edited: return 30, 'OVERLAPPING TRIPLE', False

# X WING (score: 100)

	for i in xrange(len(pairs)):
		a = pairs[i]
		for j in xrange(i):
			b = pairs[j]
			k0, k1 = a[0], b[0]
			if k0 != k1: continue

			# slicing along row
			if a[1][0][0] == b[1][0][0] and a[1][1][0] == b[1][1][0]:
				j0, j1 = a[1][0][0], a[1][1][0]
				for i in xrange(9):
					if i != a[1][0][1] and i != b[1][0][1] and k0 in opts[j0][i]:
						opts[j0][i].remove(k0)
						edited = True
					if i != a[1][1][1] and i != b[1][1][1] and k0 in opts[j1][i]:
						opts[j1][i].remove(k0)
						edited = True

			# slicing along col
			if a[1][0][1] == b[1][0][1] and a[1][1][1] == b[1][1][1]:
				j0, j1 = a[1][0][1], a[1][1][1]
				for i in xrange(9):
					if i != a[1][0][0] and i != b[1][0][0] and k0 in opts[i][j0]:
						opts[i][j0].remove(k0)
						edited = True
					if i != a[1][1][0] and i != b[1][1][0] and k0 in opts[i][j1]:
						opts[i][j1].remove(k0)
						edited = True

	if edited: return 100, 'X WING', False

# NOTHING WORKED (either we are done, or the puzzle is unsolvable)

	return -1, 'DONE', True

def score(g, verbose = False):
	'''generate a score on how advanced techniques are needed to solve'''

	score = 0
	opts = [[range(9) if g[x][y] == -1 else [] for y in xrange(9)] for x in xrange(9)]

	if verbose:
		print 'STARTING POSITION 0'
		print grid_to_string(g)

	while True:
		s, name, display = make_step(g, opts)
		if s == -1: break

		score += s
		if verbose:
			print name+' '+str(score)
			if display:
				print grid_to_string(g)
			stdout.flush()

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] == -1: return -1

	return score