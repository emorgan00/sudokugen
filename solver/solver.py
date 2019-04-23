from knight_solver import knight_score
from math import log10

def score(g, variant = 'DEFAULT', verbose = False):
	'''return the difficulty score for this puzzle.
	the score increases linearly with respect to the hardest type of tactic that has to be used.'''

	g = [[x for x in row] for row in g]
	score = None

	if variant == 'KNIGHT':
		score = knight_score(g, verbose)

	else:
		raise Exception('unsupported variant')

	return -1 if score < 0 else log10(score)