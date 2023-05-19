from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

allData = [
    [2357911, 11718061, 62468095.57, 12596033.16, 20.16, 11552, 13118, 10.58, 5.32],
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
    dados_tabela = ["VENDAS", 10, "ENTRADAS", 35.019078, 40]  # Exemplo de dados para a tabela
    dados_tabela2 = ["EVOLUÇÃO", "FAT", "100%", "RENT", "-4.47%"]  # Exemplo de dados para a segunda tabela
    soma_valores = "197.118.127,25"
    media_valores = "65.706.042,42"
    media_valor1 = "13.043.724,32"
    media_valor2 = "19,85%"
    media_valor3 = "11,468"
    media_valor4 = "45.415.813,15"
    media_valor5 = "11.121.082,14"
    media_valor6 = "4.412.847,86"
    media_valor7 = "13.432"

    return render_template('analisecomercial.html',
                           allData=allData,
                           dados_tabela=dados_tabela,
                           dados_tabela2=dados_tabela2,
                           soma_valores=soma_valores,
                           media_valores=media_valores,
                           media_valor1=media_valor1,
                           media_valor2=media_valor2,
                           media_valor3=media_valor3,
                           media_valor4=media_valor4,
                           media_valor5=media_valor5,
                           media_valor6=media_valor6,
                           media_valor7=media_valor7)


@app.route('/a')
def dashboard_a():
    dados_tabela = ["VENDAS", 10, "ENTRADAS", 35.019078, 40]  # Exemplo de dados para a tabela
    dados_tabela2 = ["EVOLUÇÃO", "FAT", "100%", "RENT", "-4.47%"]  # Exemplo de dados para a segunda tabela
    soma_valores = "197.118.127,25"
    media_valores = "65.706.042,42"
    media_valor1 = "13.043.724,32"
    media_valor2 = "119,85%"
    media_valor3 = "11,468"
    media_valor4 = "45.415.813,15"
    media_valor5 = "11.121.082,14"
    media_valor6 = "4.412.847,86"
    media_valor7 = "13.432"

    return render_template('analisecomercial.html',
                           allData=allData,
                           dados_tabela=dados_tabela,
                           dados_tabela2=dados_tabela2,
                           soma_valores=soma_valores,
                           media_valores=media_valores,
                           media_valor1=media_valor1,
                           media_valor2=media_valor2,
                           media_valor3=media_valor3,
                           media_valor4=media_valor4,
                           media_valor5=media_valor5,
                           media_valor6=media_valor6,
                           media_valor7=media_valor7)


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