import knight.grid, knight.solver
import classic.grid, classic.solver

def grid(variant):

	if variant == 'KNIGHT':
		return knight.grid()

	elif variant == 'CLASSIC':
		return classic.grid()

	else:
		raise Exception('unsupported variant')

def grid_to_string(g, variant, noFormat = False):

	if variant == 'KNIGHT':
		return knight.grid_to_string(g, noFormat)

	elif variant == 'CLASSIC':
		return classic.grid_to_string(g, noFormat)

	else:
		raise Exception('unsupported variant')

def print_grid(g, variant):

	print grid_to_string(g, variant)

def grid_from_string(g, variant):

	if variant == 'KNIGHT':
		return knight.grid_from_string(g)

	elif variant == 'CLASSIC':
		return classic.grid_from_string(g)

	else:
		raise Exception('unsupported variant')

def partial_grid(g, ratio, variant):

	if variant == 'KNIGHT':
		return knight.partial_grid(g, ratio)

	elif variant == 'CLASSIC':
		return classic.partial_grid(g, ratio)

	else:
		raise Exception('unsupported variant')