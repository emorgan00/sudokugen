from itertools import product
from sudoku import grid_from_string, grid_to_string

def formless_input(x, y):
	out = '<td class=\'sudoku_tile\'><div style=\'position: absolute; z-index: 2;\'>'
	# pencil mark numbers
	for k in xrange(1, 10):
		out += '<div class=\'pencil_mark inactive\' onclick=\'click_number(this.id);\' id=\'tile_{x}{y}_{k}\' style=\'color: rgba(0, 0, 0, 0)\'>{k}</div>'.format(x = x, y = y, k = k)
	out += '</div><div style=\'position: absolute; top: 0; bottom: 0; left: 0; right: 0; z-index: 1;\'>'
	out += '<div class=\'full_mark inactive\' id=\'tile_{x}{y}\' style=\'color: rgba(0, 0, 0, 0)\'>0</div>'.format(x = x, y = y)
	return out + '</div></td>'

def render_grid(g):
	'''render a sudoku grid as an HTML element'''

	out = '<table class=\'sudoku_container\'>'

	for x, row in enumerate(g):
		out += '<tr class=\'sudoku_row\'>'
		for y, k in enumerate(row):
			if k == -1:
				out += formless_input(x, y)
			else:
				out += '<td class=\'sudoku_tile\'><div class=\'sudoku_number\'>{}</div></td>\n'.format(k+1)
		out += '</tr>'

	return out+'</table><input type=\'hidden\' name=\'grid\' value=\'{}\'>'.format(grid_to_string(g, True))

def render_grid_pdf(g):
	'''render a sudoku grid as an HTML element, optimized for use in PDFs. Contains no form elements.'''

	out = '<table class=\'sudoku_container\'>'

	for row in g:
		out += '<tr class=\'sudoku_row\'>'
		for k in row:
			if k == -1:
				out += '<td class=\'sudoku_tile\'><div class=\'sudoku_number\'>&nbsp;</div></td>\n'
			else:
				out += '<td class=\'sudoku_tile\'><div class=\'sudoku_number\'>{}</div></td>\n'.format(k+1)
		out += '</tr>'

	return out+'</table><input type=\'hidden\' name=\'grid\' value=\'{}\'>'.format(grid_to_string(g, True))

def form_grid():
	'''render a blank fillable sudoku grid as part of an HTML form'''

	out = '<table class=\'sudoku_container\'>'

	for x in xrange(9):
		out += '<tr class=\'sudoku_row\'>'
		for y in xrange(9):
			out += '''<td class=\'sudoku_tile\'>
				<input class=\'sudoku_number sudoku_input\' name=\'tile_{}{}\' type=\'text\' maxlength=\'1\' autocomplete=\'new-password\'>
				</td>\n'''.format(x, y)
		out += '</tr>'

	return out+'</table>'

def grid_from_form(form):
	'''take a filled html form and return a standard grid. <form> should accept request.form'''

	if 'grid' in form:
		grid = grid_from_string(form['grid'])
	else:
		grid = [[-1 for _ in xrange(9)] for _ in xrange(9)]
		for x, y in product(xrange(9), xrange(9)):

			k = form['tile_{}{}'.format(x, y)]
			if k.isdigit():
				grid[x][y] = int(k)-1

	return grid