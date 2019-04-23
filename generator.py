from solver import *
from grid import *

def grid_remove(g, variant = 'DEFAULT'):
	''' given a valid sudoku, remove a number from the grid to produce another valid sudoku.
	If no such sudoku is possible, return -1. Otherwise return the new score.'''

	m_score, m_loc = -1, None

	choices = list(product(xrange(9), xrange(9)))
	shuffle(choices)

	for x, y in choices:
		if g[x][y] != -1:
			k = g[x][y]
			g[x][y] = -1
			s = score(g, variant)

			if s > m_score:
				m_score = s
				m_loc = (x, y)

			g[x][y] = k

	if m_score == -1:
		return -1

	g[m_loc[0]][m_loc[1]] = -1
	return m_score

def grid_remove_symmetric(g, style, variant = 'DEFAULT'):
	''' given a valid sudoku, remove 2 numbers from the grid in a symmetric fashion to produce another valid sudoku.
	If no such sudoku is possible, return -1. Otherwise return the new score.
	style options: H, V, R, D+, D-
	'''

	def flip(x, y):
		if style == 'V':
			return x, 8-y
		elif style == 'H':
			return 8-x, y
		elif style == 'R':
			return 8-x, 8-y
		elif style == 'D-':
			return y, x
		elif style == 'D+':
			return 8-y, 8-x


	m_score, m_loc = -1, None

	if style == 'V':
		choices = list(product(xrange(9), xrange(5)))
	elif style == 'H':
		choices = list(product(xrange(5), xrange(9)))
	elif style == 'R':
		choices = list(product(xrange(4), xrange(9)))
		for i in xrange(5):
			choices.append((4, i))
	elif style == 'D-':
		choices = []
		for i in xrange(9):
			for j in xrange(i+1):
				choices.append((i, j))
	elif style == 'D+':
		choices = []
		for i in xrange(9):
			for j in xrange(9-i):
				choices.append((i, j))
	else: raise Exception("invalid style")

	shuffle(choices)

	for x, y in choices:
		if g[x][y] != -1:
			nx, ny = flip(x, y)

			k0, k1 = g[x][y], g[nx][ny]
			g[x][y], g[nx][ny] = -1, -1

			s = score(g, variant)

			if s > m_score:
				m_score = s
				m_loc = (x, y, nx, ny)

			g[x][y], g[nx][ny] = k0, k1

	if m_score == -1:
		return -1

	g[m_loc[0]][m_loc[1]] = -1
	g[m_loc[2]][m_loc[3]] = -1
	return m_score

def generate_grid(variant = 'DEFAULT', verbose = False):
	'''randomly generate a brand new puzzle, and deconstruct it to produce a maximally difficult set of clues'''
	s, g = -1, None
	while s == -1:
		g = partial_grid(grid(variant), 0.6)
		copy = [[x for x in row] for row in g]
		s = score(copy, variant)

	while s != -1:
		if verbose:
			print s
			print_grid(g)
		s = grid_remove(g, variant)

	return g

def generate_symmetric_grid(style, variant = 'DEFAULT', verbose = False):
	'''randomly generate a brand new puzzle, and deconstruct it to produce a maximally difficult set of clues'''
	style = style.upper()
	s, g = -1, None
	while s == -1:
		g = grid(variant)
		copy = [[x for x in row] for row in g]
		s = score(copy, variant)

	while s != -1:
		if verbose:
			print s
			print_grid(g)
		s = grid_remove_symmetric(g, style, variant)

	return g