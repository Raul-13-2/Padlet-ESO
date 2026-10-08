from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Esto solo se ejecuta en tu ordenador con 'python app.py'
    app.run(debug=True)
