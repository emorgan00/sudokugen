import importlib
from math import log10

def fetch_module(variant):

	try:
		return importlib.import_module('..'+variant.lower(), __name__)
	except ImportError:
		raise Exception('unsupported variant')

def grid(variant):

	return fetch_module(variant).grid()

def grid_to_string(g, variant, noFormat = False):

	return fetch_module(variant).grid_to_string(g, noFormat)

def print_grid(g, variant, noFormat = False):

	print grid_to_string(g, variant, noFormat)

def grid_from_string(g, variant):

	return fetch_module(variant).grid_from_string(g)

def partial_grid(g, ratio, variant):

	return fetch_module(variant).partial_grid(g, ratio)