import os
from flask import *

app = Flask(__name__)

@app.route('/')
def index():

	return redirect(url_for('create'))

@app.route('/create', methods = ('GET', 'POST'))
def create():

	if request.method == 'GET':

		return render_template('create.html')

	elif request.method == 'POST':

		return render_template('display.html', variant = request.form['variant'])