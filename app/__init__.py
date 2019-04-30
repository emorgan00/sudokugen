import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from flask import *
from render import *
import sudoku

app = Flask(__name__)

# commenting a variant here will totally remove it from the site
VARIANTS = [
	# {'code': 'CLASSIC', 'name': 'Classic Sudoku'}, # commented as the algo for this is simply too weak. puzzles are too easy.
	{'code': 'KNIGHT', 'name': 'Anti-Knight Sudoku'}
]

def full_name(code):
	'''return the full name of the variant'''
	v = 'Unknown Variant'
	for d in VARIANTS:
		if d['code'] == code:
			v = d['name']
	return v

# routing

@app.route('/')
def index():

	return redirect(url_for('create'))

@app.route('/create', methods = ('GET', 'POST'))
def create():

	if request.method == 'GET':

		return render_template(
			'create.html',
			title = 'Generator',
			variants = VARIANTS
		)

	elif request.method == 'POST':

		v = request.form['variant']
		s = request.form['symmetry']
		m = request.form['difficulty']

		try: m = float(m)
		except: m = None

		if request.form['symmetry'] == 'N':
			g = sudoku.generate_grid(v, m)
		else:
			g = sudoku.generate_symmetric_grid(s, v, m)
		return render_template(
			'display.html',
			title = 'Generator',
			puzzle = render_grid(g),
			variant = full_name(request.form['variant']),
			difficulty = sudoku.score(g, v),
			code = sudoku.grid_to_string(g, True)
		)

@app.route('/solve', methods = ('GET', 'POST'))
def solve():

	if request.method == 'GET':

		return render_template(
			'solve.html',
			title = 'Solver',
			variants = VARIANTS,
			puzzle = form_grid()
		)

	elif request.method == 'POST':

		v = request.form['variant']
		g = grid_from_form(request.form)
		sc = sudoku.score(g, v)
		if request.form['submit_type'] == 'Solve': sudoku.solve(g, v)

		return render_template(
			'display.html',
			title = 'Solver',
			puzzle = render_grid(g),
			variant = full_name(request.form['variant']),
			difficulty = sc,
			code = sudoku.grid_to_string(g, True)
		)

@app.route('/pdf', methods = ['POST'])
def pdf():
	
	from flask_weasyprint import HTML, render_pdf

	html = render_template(
		'grid_pdf.html',
		puzzle = render_grid_pdf(grid_from_string(request.form['code'])),
		variant = request.form['variant'], # should contain full name, not short name
		difficulty = request.form['difficulty']
	)
	return render_pdf(HTML(string = html))