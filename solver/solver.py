from knight_solver import knight_score

def score(g, variant = 'DEFAULT', verbose = False):

	if variant == 'KNIGHT':
		return knight_score(g, verbose)

	else:
		raise Exception('unsupported variant')