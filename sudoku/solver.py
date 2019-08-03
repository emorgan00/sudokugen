from headers import fetch_module

def score(g, variant, verbose = False):
	'''return the difficulty score for this puzzle.
	the score increases linearly with respect to the hardest type of tactic that has to be used.'''

	return solve([row[:] for row in g], variant, verbose)

def solve(g, variant, verbose = False):
	'''solve this puzzle.'''

	module = fetch_module(variant)

	