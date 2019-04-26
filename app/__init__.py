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
		if request.form['symmetry'] == 'N':
			g  = generate_grid(request.form['variant'])
		else:
			g  = generate_symmetric_grid(request.form['symmetry'], request.form['variant'])
		return render_template(
			'display.html',
			puzzle = render_grid(g),
			variant = request.form['variant'],
			symmetry = request.form['symmetry'],
			difficulty = score(g, request.form['variant'])
		)