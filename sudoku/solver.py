from math import log10
from knight_solver import *
from classic_solver import *

def score(g, variant = 'CLASSIC', verbose = False):
	'''return the difficulty score for this puzzle.
	the score increases linearly with respect to the hardest type of tactic that has to be used.'''

	g = [[x for x in row] for row in g]
	score = None

	if variant == 'KNIGHT':
		score = knight_score(g, verbose)

	elif variant == 'CLASSIC':
		score = classic_score(g, verbose)

	else:
		raise Exception('unsupported variant')

	return -1 if score <= 0 else round(log10(score), 2)

def solve(g, variant = 'CLASSIC', verbose = False):
	'''solve this puzzle.'''

	if variant == 'KNIGHT':
		knight_score(g, verbose)

	elif variant == 'CLASSIC':
		classic_score(g, verbose)

	else:
		raise Exception('unsupported variant')