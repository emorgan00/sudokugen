from grid import *
from itertools import product

def score(g, variant = 'DEFAULT', verbose = False):
	'''generate a score on how advanced techniques are needed to solve'''
	score = 0
	global opts

	def add(x, y, k, opts, v = 'DEFAULT'): # for manual adding
		g[x][y] = k
		for i, j in neighbors_all(x, y, v):
			if k in opts[i][j]:
				opts[i][j].remove(k)


	def elim(): # a box is in direct conflict with 8 other numbers.
		global opts

		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1: continue
			if len(opts[x][y]) == 0:
				raise Exception("No solution")
			if len(opts[x][y]) == 1:
				g[x][y] = opts[x][y][0]
				return True

		return False

	def slice(): # a box/row/col only has 1 spot where the number can go
		global opts

		def check_group(group):
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
			if check_group(product(xrange(cx, cx+3), xrange(cy, cy+3))): return True

		# rows/cols
		for i in xrange(9):
			if check_group(product([i], xrange(9))): return True
			if check_group(product(xrange(9), [i])): return True

		return False

	def check():
		if elim(): return 'ELIM'
		if slice(): return 'SLICE'
		return None

	def setup_opts(special = False):
		global opts

		opts = [[range(9) for _ in xrange(9)] for _ in xrange(9)]
		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1:
				add(x, y, g[x][y], opts, variant if special else 'DEFAULT')

	def implicit_opts(): # a pair slicing another box/row/col
		global opts

		# precondition: opts is already setup with setup_opts

		def check_group(group):
			edited = False
			count = [[] for _ in xrange(9)]
			for x, y in group:
				if g[x][y] != -1: continue
				for k in opts[x][y]:
					count[k].append((x, y))
			
			for k in xrange(9):
				if len(count[k]) != 2: continue
				if count[k][0][0] == count[k][1][0]: # same y, slice along x
					i = count[k][0][0]
					for j in xrange(9):
						if j != count[k][0][1] and j != count[k][1][1] and k in opts[i][j]:
							opts[i][j].remove(k)
							edited = True
				if count[k][0][1] == count[k][1][1]: # same x, slice along y
					j = count[k][0][1]
					for i in xrange(9):
						if i != count[k][0][0] and i != count[k][1][0] and k in opts[i][j]:
							opts[i][j].remove(k)
							edited = True
			return edited

		flag = False
		for cx, cy in product(xrange(0, 9, 3), xrange(0, 9, 3)):
			if check_group(product(xrange(cx, cx+3), xrange(cy, cy+3))): flag = True

		return flag

	msg = 'STARTING POSITION'
	while True:

		if verbose:
			print msg+' '+str(score)
			print_grid(g)

		# Check for elims/slices
		setup_opts(False)

		c = check()
		if c:
			if verbose: msg = c
			score += 1; continue

		implicit_opts()

		c = check()
		if c:
			if verbose: msg = 'IMPLICIT '+c
			score += 5; continue

		if variant == 'DEFAULT': break

		# Check for variant elims/slices
		setup_opts(True)

		c = check()
		if c:
			if verbose: msg = 'VARIANT '+c
			score += 5; continue

		implicit_opts()

		c = check()
		if c:
			if verbose: msg = 'VARIANT IMPLICIT '+c;
			score += 50; continue

		break

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] == -1: return -1

	return score