from flask import Flask, render_template, jsonify
import requests
import csv
url = "https://docs.google.com/spreadsheets/d/1sfp7PK89RgPgktWJJDREiZKOrSq_W8Jzx020GBvuq0A/export?format=csv"
app = Flask(__name__)
class deure:
    def __init__(self, titol, deure, data):
        self.titol = titol
        self.fer = deure
        self.data = data

lineas = (linea.decode("utf-8") for linea in requests.get(url).iter_lines())
lector = csv.DictReader(lineas)
deures = [deure(linea["Titol"], linea["Deure"], linea["Data"]) for linea in lector]

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
    lista = []
    for deure in deures:
        lista.append({"titol": deure.titol, "fer": deure.fer})
    return jsonify(lista)

if __name__ == '__main__':
    # Esto solo se ejecuta en tu ordenador con 'python app.py'
    app.run(debug=True)
