from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

allData = [
    [112357911, 11718061, 62468095.57, 12596033.16, 20.16, 11552, 13118, 10.58, 5.32],
    [11896319, 11183848, 61055572.19, 12859511.51, 21.06, 11353, 12949, 11.13, 5.46],
    [13589381, 11961338, 68567964.06, 14712653.97, 21.46, 11411, 13319, 11.14, 5.73],
    [12237109, 12020019, 71098304.87, 14210656.16, 19.99, 11475, 13050, 11.19, 5.91],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

]


@app.route('/')
def dashboard():
    return render_template('analisecomercial.html', allData=allData)


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