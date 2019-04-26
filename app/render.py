def render_grid(g):
	'''render a sudoku grid as an HTML element'''

	out = '<table class = \'sudoku_container\'>'

	for row in g:
		out += '<tr class = \'sudoku_row\'>'
		for x in row:
			out += '''<td class = \'sudoku_tile\'><div class = \'sudoku_number\'>{}</div></td>'''.format(x+1 if x != -1 else ' ')
		out += '</tr>'

	return out+'</div>'
