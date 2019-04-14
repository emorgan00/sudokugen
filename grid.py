from random import shuffle, random

def grid(variant = 'DEFAULT'):
	'''Variants: 'DEFAULT', 'KNIGHT' '''
	variant = variant.upper()

	grid = [[None for _ in xrange(9)] for _ in xrange(9)]
	opts = [[range(9) for _ in xrange(9)] for _ in xrange(9)]

	def add(x, y, k): # for manual adding
		grid[x][y] = k
		for i, j in neighbors_all(x, y):
			if k in opts[i][j]:
				opts[i][j].remove(k)

	def neighbors(x, y): # return proceeding cells which are in conflict with (x, y)
		# horizontal / vertical
		out = []
		for i in xrange(9):
			if i > x: yield (i, y)
			if i > y: yield (x, i)
		# within box
		cx, cy = x/3*3, y/3*3 # corner of square
		for i in xrange(cx, cx+3):
			for j in xrange(y+1, cy+3):
				yield (i, j)
		# knight moves: a special variation
		if variant == 'KNIGHT':
			for dx, dy in [(2, 1), (-2, 1), (1, 2), (-1, 2)]:
				i, j = x+dx, y+dy
				if i >= 0 and j >= 0 and i < 9 and j < 9:
					yield (i, j)

	def neighbors_all(x, y): # return all cells which are in conflict with (x, y)
		# horizontal / vertical
		out = []
		for i in xrange(9):
			yield (i, y)
			yield (x, i)
		# within box
		cx, cy = x/3*3, y/3*3 # corner of square
		for i in xrange(cx, cx+3):
			for j in xrange(cy, cy+3):
				yield (i, j)
		# # knight moves: a special variation
		if variant == 'KNIGHT':
			for dx, dy in [(2, 1), (-2, 1), (1, 2), (-1, 2), (2, -1), (-2, -1), (1, -2), (-1, -2)]:
				i, j = x+dx, y+dy
				if i >= 0 and j >= 0 and i < 9 and j < 9:
					yield (i, j)

	def fill(x, y):
		if y == 9: return True
		n = list(neighbors(x, y))
		rm = []
		nx, ny = (x+1)%9, y+1 if x == 8 else y
		if grid[x][y] != None:
			return fill(nx, ny)

		shuffle(opts[x][y])
		for k in opts[x][y]:

			grid[x][y] = k
			for i, j in n:
				if k in opts[i][j]:
					opts[i][j].remove(k)
					rm.append((i, j))

			if fill(nx, ny): return True

			while rm:
				i, j = rm.pop()
				opts[i][j].append(k)

		grid[x][y] = None
		return False

	fill(0, 0)
	return grid

def print_grid(g):
	for row in g: print ' '.join('.' if x == -1 else str(x+1) for x in row)

def partial_grid(g, ratio):
	return [[x if random() < ratio else -1 for x in row] for row in g]