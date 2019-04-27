def render_grid(g):
	'''render a sudoku grid as an HTML element'''

	out = '<table class=\'sudoku_container\'>'

	for row in g:
		out += '<tr class=\'sudoku_row\'>'
		for x in row:
			if x == -1:
				out += '''<td class=\'sudoku_tile\'><input class=\'sudoku_input\' type=\'text\' maxlength=\'1\' pattern=\'^[0-9]$\'></td>'''
			else:
				out += '''<td class=\'sudoku_tile\'><div class=\'sudoku_number\'>{}</div></td>'''.format(x+1)
		out += '</tr>'

	return out+'</div>'

def form_grid():
	'''render a fillable sudoku grid as an HTML form'''

	out = '<form class=\'sudoku_form\'><table class=\'sudoku_container\'>'

	for _ in xrange(9):
		out += '<tr class=\'sudoku_row\'>'
		for _ in xrange(9):
			out += '''<td class=\'sudoku_tile\'><input class=\'sudoku_input\' type=\'text\' maxlength=\'1\' pattern=\'^[0-9]$\'></td>'''
		out += '</tr>'

	return out+'</div></form>'

