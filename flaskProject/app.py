from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('analisecomercial.html')

@app.route('/faturamento')
def faturamento():
    return render_template('faturamento.html')

if __name__ == '__main__':
    app.run(debug=True)