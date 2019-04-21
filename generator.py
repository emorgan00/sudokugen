from solver import *

def grid_remove(g, variant = 'DEFAULT'):
	''' given a valid sudoku, remove a number from the grid to produce another valid sudoku.
	If no such sudoku is possible, return -1. Otherwise return the new score.'''

	m_score, m_loc = -1, (0, 0)

	choices = list(product(xrange(9), xrange(9)))
	shuffle(choices)

	for x, y in choices:
		if g[x][y] != -1:
			copy = [[k if j != y or i != x else -1 for j, k in enumerate(row)] for i, row in enumerate(g)]
			s = score(copy, variant)

			if s > m_score:
				m_score = s
				m_loc = (x, y)

	if m_score == -1:
		return -1

	g[m_loc[0]][m_loc[1]] = -1
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