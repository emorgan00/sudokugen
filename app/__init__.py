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

		return render_template('display.html', variant = render_grid(grid(request.form['variant'])))