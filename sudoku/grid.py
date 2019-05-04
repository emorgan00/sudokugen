import knight.grid, knight.solver
import classic.grid, classic.solver
import between.grid

def grid(variant):

	variant = variant.upper()

	if variant == 'KNIGHT':
		return knight.grid()

	elif variant == 'CLASSIC':
		return classic.grid()

	elif variant == 'BETWEEN':
		return between.grid()

	else:
		raise Exception('unsupported variant')

def grid_to_string(g, variant, noFormat = False):

	variant = variant.upper()

	if variant == 'KNIGHT':
		return knight.grid_to_string(g, noFormat)

	elif variant == 'CLASSIC':
		return classic.grid_to_string(g, noFormat)

	elif variant == 'BETWEEN':
		return between.grid_to_string(g, noFormat)

	else:
		raise Exception('unsupported variant')

def print_grid(g, variant):

	print grid_to_string(g, variant)

def grid_from_string(g, variant):

	variant = variant.upper()

	if variant == 'KNIGHT':
		return knight.grid_from_string(g)

	elif variant == 'CLASSIC':
		return classic.grid_from_string(g)

	elif variant == 'BETWEEN':
		return between.grid_from_string(g)

	else:
		raise Exception('unsupported variant')

def partial_grid(g, ratio, variant):

	variant = variant.upper()

	if variant == 'KNIGHT':
		return knight.partial_grid(g, ratio)

	elif variant == 'CLASSIC':
		return classic.partial_grid(g, ratio)

	elif variant == 'BETWEEN':
		return between.partial_grid(g, ratio)

	else:
		raise Exception('unsupported variant')