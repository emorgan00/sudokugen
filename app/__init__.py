import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from flask import *
from render import *
from flask_weasyprint import HTML, render_pdf
import sudoku

app = Flask(__name__)

VARIANTS = [
	{'code': 'KNIGHT', 'name': 'Knight Sudoku'}
]

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
			variant = v,
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
		sudoku.solve(g, 'KNIGHT') # this needs to be updated

		return render_template(
			'display.html',
			title = 'Solver',
			puzzle = render_grid(g),
			variant = v,
			difficulty = sc,
			code = sudoku.grid_to_string(g, True)
		)

@app.route('/pdf', methods = ['POST'])
def pdf():

	html = render_template(
		'grid_pdf.html',
		puzzle = render_grid(grid_from_string(request.form['code'])),
		variant = request.form['variant']
	)
	return render_pdf(HTML(string = html))