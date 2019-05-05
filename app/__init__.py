import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from flask import *
from render import *
from compress import *
import sudoku

app = Flask(__name__)

# commenting a variant here will totally remove it from the site
VARIANTS = [
	{'code': 'CLASSIC', 'name': 'Classic Sudoku'},
	{'code': 'KNIGHT', 'name': 'Anti-Knight Sudoku'},
	{'code': 'BETWEEN', 'name': 'Between 1 & 9 Sudoku (in development)'}
]

def full_name(code):
	'''return the full name of the variant'''
	code = code.upper()
	for d in VARIANTS:
		if d['code'] == code:
			return d['name']
	return 'Unknown Variant'

# routing

@app.route('/')
def index():

	return redirect(url_for('about'))

@app.route('/about', methods = ['GET'])
def about():

	return render_template(
		'about.html'
	)

@app.route('/create', methods = ['GET', 'POST'])
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

		code = sudoku.grid_to_string(g, v, True)

		return render_template(
			'display.html',
			title = 'Generator',
			puzzle = render_grid(g, v),
			v_code = v,
			variant = full_name(v),
			difficulty = sudoku.score(g, v),
			code = code,
			c_code = compress_code(code)
		)

@app.route('/solve', methods = ['GET', 'POST'])
def solve():

	if request.method == 'GET':

		v = request.args.get('v')
		if v == None: v = 'CLASSIC'
		else: v = v.upper()

		return render_template(
			'solve.html',
			title = 'Solver',
			variants = VARIANTS,
			puzzle = form_grid(v),
			v_code = v
		)

	elif request.method == 'POST':

		v = request.form['variant']
		g = grid_from_form(request.form, v)
		code = sudoku.grid_to_string(g, v, True)

		sc = None
		if request.form['submit_type'] == 'Solve':
			sc = sudoku.solve(g, v)
		else:
			sc = sudoku.score(g, v)

		return render_template(
			'display.html',
			title = 'Solver',
			puzzle = render_grid(g, v),
			variant = full_name(v),
			v_code = v,
			difficulty = sc,
			code = code,
			c_code = compress_code(code)
		)

@app.route('/pdf', methods = ['POST'])
def pdf():
	
	from flask_weasyprint import HTML, render_pdf

	v = request.form['variant'] # should contain short name, not full name

	html = render_template(
		'grid_pdf.html',
		puzzle = render_grid_pdf(sudoku.grid_from_string(request.form['code'], v), v),
		variant = full_name(v),
		difficulty = request.form['difficulty']
	)
	return render_pdf(HTML(string = html))

@app.route('/load/<v>/<code>', methods = ['GET'])
def load(v, code):

	if any(c not in '.123456789' for c in code):
		code = decompress_code(code)

	g = grid_from_string(code, v);
	code = sudoku.grid_to_string(g, v, True)

	return render_template(
		'display.html',
		title = 'Load Puzzle',
		puzzle = render_grid(g, v),
		variant = full_name(v),
		v_code = v.upper(),
		difficulty = sudoku.score(g, v),
		code = code,
		c_code = compress_code(code)
	)