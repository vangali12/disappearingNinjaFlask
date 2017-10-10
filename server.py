from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
def display():
	return render_template('index.html')

@app.route('/ninja')
def showNinjas():
	return render_template('ninjas.html')

@app.route('/ninja/<color>')
def showProfile(color):
	if (color == 'blue'):
		return render_template('blue.html')
	elif (color == 'purple'):
		return render_template('purple.html')
	elif (color == 'red'):
		return render_template('red.html')
	elif (color =='orange'):
		return render_template('orange.html')
	else:
		return render_template('notApril.html')

app.run(debug=True)