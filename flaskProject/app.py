from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)


@app.route('/')
def index():
    # Ler os dados do arquivo CSV
    data = pd.read_csv('data.csv')

    graphs = []
    for i in range(5):
        # Filtrar os dados para cada linha
        row_data = data.iloc[i - 1]

        # Criar um DataFrame com os dados da linha
        df = pd.DataFrame({
            'Mes': list(range(1, 13)),
            'ITENSENTRADA': [row_data['ITENSENTRADA']] * 12,
            'ITENSVENDIDOS': [row_data['ITENSVENDIDOS']] * 12,
            'Faturamento': [row_data['Faturamento']] * 12,
            'Rentabilidade': [row_data['Rentabilidade']] * 12,
            'FxR': [row_data['FxR']] * 12,
            'sku': [row_data['sku']] * 12,
            'SKUESTOQUE': [row_data['SKUESTOQUE']] * 12
        })

        # Criar um gráfico de linhas para cada coluna
        fig = px.line(df, x='Mes',
                      y=['ITENSENTRADA', 'ITENSVENDIDOS', 'Faturamento', 'Rentabilidade', 'sku', 'SKUESTOQUE'],
                      title=f'Gráfico {i}', labels={'value': 'Valores', 'variable': 'Categoria'})

        # Converter o gráfico para HTML e adicionar à lista de gráficos
        graph_div = pio.to_html(fig, full_html=False)
        graphs.append(graph_div)

    return render_template('index.html', graphs=graphs)

if __name__ == '__main__':
    app.run(debug=True)


