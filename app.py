from flask import Flask, render_template
import requests

app = Flask(__name__)
class deure:
    def __init__(self, titol, deure):
        self.titol = titol
        self.fer = deure

vacio = deure("","")

@app.route('/')
def index():
    return render_template('index.html', deure=vacio)

if __name__ == '__main__':
    # Esto solo se ejecuta en tu ordenador con 'python app.py'
    app.run(debug=True)
