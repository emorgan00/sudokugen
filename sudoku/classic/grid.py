from random import shuffle, random
from itertools import product

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

def same_box(ax, ay, bx, by): # return the box corner if the two coordinates are in the same box, False otherwise
	if ax/3 == bx/3 and ay/3 == by/3:
		return ax/3*3, ay/3*3
	return False

def in_range(x, y):
	return x >= 0 and y >= 0 and x < 9 and y < 9

def grid():

	grid = [[None for _ in xrange(9)] for _ in xrange(9)]
	opts = [[range(9) for _ in xrange(9)] for _ in xrange(9)]

	def add(x, y, k): # for manual adding
		grid[x][y] = k
		for i, j in neighbors_all(x, y):
			if k in opts[i][j]:
				opts[i][j].remove(k)

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

def grid_to_string(g, noformat = False):
	'''return the grid represented as a string. If <noformat> is True, then there will be no whitespace in the returned string.'''
	if noformat:
		return ''.join(''.join('.' if x == -1 else str(x+1) for x in row) for row in g)
	else:
		return '\n'.join(' '.join('.' if x == -1 else str(x+1) for x in row) for row in g)

def partial_grid(g, ratio):
	return [[x if random() < ratio else -1 for x in row] for row in g]

def grid_from_string(s):
	out = [[-1 for _ in xrange(9)] for _ in xrange(9)]
	s = s.strip().replace('\n', '').replace(' ', '')
	while len(s) < 81: s += '.'
	for x, y in product(xrange(9), xrange(9)):
		out[x][y] = int(s[x*9+y])-1 if s[x*9+y].isdigit() else -1 
	return out