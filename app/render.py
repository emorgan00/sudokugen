from itertools import product

def render_grid(g):
	'''render a sudoku grid as an HTML element'''

	out = '<table class=\'sudoku_container\'>'

	for row in g:
		out += '<tr class=\'sudoku_row\'>'
		for x in row:
			if x == -1:
				out += '<td class=\'sudoku_tile\'><input class=\'sudoku_input\' type=\'text\' maxlength=\'1\'></td>\n'
			else:
				out += '<td class=\'sudoku_tile\'><div class=\'sudoku_number\'>{}</div></td>\n'.format(x+1)
		out += '</tr>'

	return out+'</div>'

def form_grid():
	'''render a fillable sudoku grid as part of an HTML form'''

	out = '<table class=\'sudoku_container\'>'

	for x in xrange(9):
		out += '<tr class=\'sudoku_row\'>'
		for y in xrange(9):
			out += '<td class=\'sudoku_tile\'><input class=\'sudoku_input\' name=\'{}{}\' type=\'text\' maxlength=\'1\'></td>\n'.format(x, y)
		out += '</tr>'

	return out+'</div>'

def grid_from_form(form):
	'''take a filled html form and return a standard grid. <form> should accept request.form'''

	grid = [[-1 for _ in xrange(9)] for _ in xrange(9)]

	for x, y in product(xrange(9), xrange(9)):

		k = form['{}{}'.format(x, y)]
		if k.isdigit():
			grid[x][y] = int(k)-1

	return grid
