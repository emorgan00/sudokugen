from grid import *
from itertools import product

def score(g, variant = 'DEFAULT'):
	'''generate a score on how advanced techniques are needed to solve'''
	score = 0

	def add(x, y, k, opts, v = 'DEFAULT'): # for manual adding
		g[x][y] = k
		for i, j in neighbors_all(x, y, v):
			if k in opts[i][j]:
				opts[i][j].remove(k)

	def default_elim(): # score: 1

		opts = [[range(9) for _ in xrange(9)] for _ in xrange(9)]
		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1:
				add(x, y, g[x][y], opts)

		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1: continue
			if len(opts[x][y]) == 0:
				raise Exception("No solution")
			if len(opts[x][y]) == 1:
				g[x][y] = opts[x][y][0]
				return True

		return False

	def special_elim(): # score: 10

		opts = [[range(9) for _ in xrange(9)] for _ in xrange(9)]
		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1:
				add(x, y, g[x][y], opts, variant)

		for x, y in product(xrange(9), xrange(9)):
			if g[x][y] != -1: continue
			if len(opts[x][y]) == 0:
				raise Exception("No solution")
			if len(opts[x][y]) == 1:
				g[x][y] = opts[x][y][0]
				return True

		return False

	flag = True
	while flag:
		if default_elim():
			score += 1
			continue
		if special_elim():
			score += 10
			continue
		flag = False

	return score

puzzle = grid('knight')
puzzle = partial_grid(puzzle, 0.4)
print_grid(puzzle)

print score(puzzle, 'KNIGHT')
print_grid(puzzle)

		