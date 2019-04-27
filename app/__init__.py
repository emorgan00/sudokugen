import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from flask import *
from render import *
from sudoku import *

app = Flask(__name__)

@app.route('/')
def index():

	return redirect(url_for('create'))

@app.route('/create', methods = ('GET', 'POST'))
def create():

	if request.method == 'GET':

		return render_template('create.html')

	elif request.method == 'POST':

		v = request.form['variant']
		s = request.form['symmetry']
		m = request.form['difficulty']

		try: m = float(m)
		except: m = None

		if request.form['symmetry'] == 'N':
			g = generate_grid(v, m)
		else:
			g = generate_symmetric_grid(s, v, m)
		return render_template(
			'display.html',
			puzzle = render_grid(g),
			variant = v,
			symmetry = s,
			difficulty = score(g, v)
		)

@app.route('/solve', methods = ('GET', 'POST'))
def solve():

	if request.method == 'GET':

		return render_template('solve.html', puzzle = form_grid())

	elif request.method == 'POST':

		return 'Coming Soon.\n'+str(grid_from_form(request.form))