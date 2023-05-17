from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('analisecomercial.html')

@app.route('/faturamento')
def faturamento():
    return render_template('faturamento.html')

@app.route('/importar_csv')
def importar_csv():
    arquivo_csv = 'alldata2016.csv'
    dados = pd.read_csv(arquivo_csv, delimiter=';')
    # Resto do código para manipular os dados do CSV
    return 'CSV importado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
