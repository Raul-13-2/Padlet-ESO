from flask import Flask, render_template
import requests

app = Flask(__name__)
class deure:
    def __init__(self, titol, deure):
        self.titol = titol
        self.fer = deure

vacio = deure("Mates","Fer expliquem 1, 2, 3, 4")
deures = [vacio]

@app.route('/')
def index():
    return render_template('index.html', deures=deures)

@app.route('/mates')
def mates():
    return render_template('mates.html')

@app.route('/chomik')
def chomik():
    return render_template('chomik.html')

@app.route("/api")
def api():
    return deures

if __name__ == '__main__':
    # Esto solo se ejecuta en tu ordenador con 'python app.py'
    app.run(debug=True)
