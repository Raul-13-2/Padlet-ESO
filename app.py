from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola Mundo! Mi app ya funciona en Render."

if __name__ == '__main__':
    # Esto solo se ejecuta en tu ordenador con 'python app.py'
    app.run(debug=True)
