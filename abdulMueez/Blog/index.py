
from flask import Flask,render_template

app = Flask(__name__,template_folder='template')

@app.route('/hello')
def lhue():
    return render_template('/index.html')

@app.route('/style')
def style():
    return render_template('/style.html')

@app.route('/design')
def design():
    return render_template('/design.html')

@app.route('/food')
def food():
    return render_template('/food.html')

@app.route('/music')
def music():
    return render_template('/music.html')

@app.route('/people')
def people():
    return render_template('/people.html')

@app.route('/sports')
def sports():
    return render_template('/sports.html')

@app.route('/technology')
def technology():
    return render_template('/technology.html')

@app.route('/travel')
def travel():
    return render_template('/travel.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
