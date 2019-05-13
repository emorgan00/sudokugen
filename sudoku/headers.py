import importlib
from math import log10

def fetch_module(variant):

	try:
		return importlib.import_module('..'+variant.lower(), __name__)
	except ImportError:
		raise Exception('unsupported variant')

def score(g, variant, verbose = False):
	'''return the difficulty score for this puzzle.
	the score increases linearly with respect to the hardest type of tactic that has to be used.'''

	g = [[x for x in row] for row in g]
	return solve(g, variant, verbose)

def solve(g, variant, verbose = False):
	'''solve this puzzle.'''

	score = fetch_module(variant).score(g, verbose)

	if score == 0: return 0
	if score < 0: return -1
	return round(log10(score), 2)

def grid(variant):

	return fetch_module(variant).grid()

def grid_to_string(g, variant, noFormat = False):

	return fetch_module(variant).grid_to_string(g, noFormat)

def print_grid(g, variant):

	print grid_to_string(g, variant)

def grid_from_string(g, variant):

	return fetch_module(variant).grid_from_string(g)

def partial_grid(g, ratio, variant):

	return fetch_module(variant).partial_grid(g, ratio)