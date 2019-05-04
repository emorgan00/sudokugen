from itertools import product
from sudoku import grid_from_string, grid_to_string

def formless_input(x, y, k):
	'''special codes for k: 
	-1: blank, but uneditable
	-2: 0, but actually draw the 0'''

	out = '<td class="sudoku_tile"><div style="position: absolute; z-index: 2; top: 0; bottom: 0; left: 0; right: 0;">'
	# pencil mark numbers
	for k0 in xrange(1, 10):
		out += '''<div class="pencil_mark inactive" onclick="click_number(this.id, event.shiftKey, {editable});" id="tile_{x}{y}_{k}" style="color: rgba(0, 0, 0, 0)">
				<text style="position: absolute; left: 0; right: 0; margin: auto;">{k}</text>
			</div>'''.format(x = x, y = y, k = k0, editable = 'true' if k == 0 else 'false')
	out += '</div><div style="position: absolute; top: 0; bottom: 0; left: 0; right: 0; z-index: 1;">'

	if k == 0:
		out += '<div class="full_mark inactive" id="tile_{x}{y}" style="color: rgba(0, 0, 0, 0)">0</div>'.format(x = x, y = y)
	else:
		k = 0 if k == -2 else '&nbsp;' if k == -1 else k
		out += '<div class="full_mark immutable" id="tile_{x}{y}" style="color: #000000;">{k}</div>'.format(x = x, y = y, k = k)

	return out + '</div></td>'

def render_grid(g, v):
	'''render a sudoku grid as an HTML element'''

	if v.upper() in ('CLASSIC', 'KNIGHT'):
		out = '<table class="sudoku_container" id="sudoku_container">'

		for x, row in enumerate(g):
			out += '<tr class="sudoku_row">'
			for y, k in enumerate(row):
				out += formless_input(x, y, k+1)
			out += '</tr>'

		return out+'</table><input type="hidden" name="grid" value="{}">'.format(grid_to_string(g, v, True))

	if v.upper() in ('BETWEEN'):
		out = '<table class="sudoku_container" id="sudoku_container">'

		out += '<tr class="sudoku_row">'
		out += formless_input(9, 0, -1)
		for y, k in enumerate(g[9]):
			out += formless_input(9, y+1, -2 if k == 0 else k)
		out += '</tr>'

		for x, row in enumerate(g[:9]):
			out += '<tr class="sudoku_row">'
			out += formless_input(10, x, -2 if g[10][x] == 0 else g[10][x])
			for y, k in enumerate(row):
				out += formless_input(x, y, k+1)
			out += '</tr>'

		return out+'</table><input type="hidden" name="grid" value="{}">'.format(grid_to_string(g, v, True))

def render_grid_pdf(g, v):
	'''render a sudoku grid as an HTML element, optimized for use in PDFs. Contains no form elements.'''

	out = '<table class="sudoku_container">'

	for row in g:
		out += '<tr class="sudoku_row">'
		for k in row:
			if k == -1:
				out += '<td class="sudoku_tile"><div class="sudoku_number">&nbsp;</div></td>\n'
			else:
				out += '<td class="sudoku_tile"><div class="sudoku_number">{}</div></td>\n'.format(k+1)
		out += '</tr>'

	return out+'</table><input type="hidden" name="grid" value="{}">'.format(grid_to_string(g, v, True))

def form_grid(v):
	'''render a blank fillable sudoku grid as part of an HTML form'''

	if v.upper() in ('CLASSIC', 'KNIGHT'):
		out = '<table class="sudoku_container">'

		for x in xrange(9):
			out += '<tr class="sudoku_row">'
			for y in xrange(9):
				out += '''<td class="sudoku_tile">
					<input class="sudoku_number sudoku_input" name="tile_{}{}" type="text" maxlength="1" autocomplete="new-password">
					</td>\n'''.format(x, y)
			out += '</tr>'

		return out+'</table>'

	if v.upper() in ('BETWEEN'):

		return ''

def grid_from_form(form, v):
	'''take a filled html form and return a standard grid. <form> should accept request.form'''

	if 'grid' in form:
		grid = grid_from_string(form['grid'], v)
	else:
		grid = [[-1 for _ in xrange(9)] for _ in xrange(9)]
		for x, y in product(xrange(9), xrange(9)):

			k = form['tile_{}{}'.format(x, y)]
			if k.isdigit():
				grid[x][y] = int(k)-1

	return grid