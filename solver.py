from grid import *
from itertools import product

def score(g, variant = 'DEFAULT', verbose = False):
	'''generate a score on how advanced techniques are needed to solve'''
	score = 0

	def add(x, y, k, opts, v = 'DEFAULT'): # for manual adding
		g[x][y] = k
		for i, j in neighbors_all(x, y, v):
			if k in opts[i][j]:
				opts[i][j].remove(k)

	def elim(special = False): # a box is in direct conflict with 8 other numbers.

		opts = [[range(9) for _ in xrange(9)] for _ in xrange(9)]
		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1:
				add(x, y, g[x][y], opts, variant if special else 'DEFAULT')

		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1: continue
			if len(opts[x][y]) == 0:
				raise Exception("No solution")
			if len(opts[x][y]) == 1:
				g[x][y] = opts[x][y][0]
				return True

		return False

	def slice(special = False): # a box/row/col only has 1 spot where the number can go

		opts = [[range(9) for _ in xrange(9)] for _ in xrange(9)]
		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1:
				add(x, y, g[x][y], opts, variant if special else 'DEFAULT')

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

	flag = True
	msg = 'STARTING POSITION'
	while flag:
		if verbose:
			print msg
			print_grid(puzzle)
		if elim(False):
			if verbose: msg = 'DEFAULT ELIM'
			score += 1
			continue
		if slice(False):
			if verbose: msg = 'DEFAULT SLICE'
			score += 1
			continue
		if elim(True):
			if verbose: msg = 'SPECIAL ELIM'
			score += 10
			continue
		if slice(True):
			if verbose: msg = 'SPECIAL SLICE'
			score += 10
			continue
		flag = False

	for x, y in product(xrange(9), xrange(9)):
		if g[x][y] == -1: return -1

	return score

'''
puzzle = [
	[-1, -1, -1, -1, -1, -1, -1, -1,  2],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1,  2, -1, -1, -1],
	[-1, -1, -1, -1,  2, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1,  2, -1, -1],
	[-1,  3, -1, -1, -1, -1, -1, -1, -1],
	[-1,  4, -1, -1, -1, -1, -1, -1, -1],
	[-1,  5, -1, -1, -1, -1, -1, -1, -1],
	[-1,  6, -1, -1, -1, -1, -1, -1, -1]
]

print score(puzzle)
print_grid(puzzle)
'''


puzzle = grid('knight')
print_grid(puzzle)
puzzle = partial_grid(puzzle, 0.3)

print score(puzzle, 'KNIGHT', True)
print_grid(puzzle)