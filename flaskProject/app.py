from flask import Flask, render_template, request
import pandas as pd
import graficos as gr
import numpy as np

app = Flask(__name__)

allData = [
    # 2023 analise comercial
    [235791, 11718061, 62468095.57, 12596033.16, 20.16, 11552, 13118, 10.58, 5.32],
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

allData2 = [
    # 2022 analise comercial
    [43, 1234504, 9567205.57, 1245233.16, 22.16, 15840, 24128, 12.58, 6.32],
    [578244, 936292, 7885899.19, 1383722.51, 24.06, 16741, 21049, 14.13, 7.46],
    [894502, 842509, 5796122.06, 1512367.97, 23.46, 14251, 16319, 15.14, 6.73],
    [764802, 915710, 6760894.87, 1470196.16, 21.99, 13752, 16560, 16.19, 7.01],
    [951331, 868602, 6842430.90, 1435532.40, 20.40, 13658, 15871, 14.92, 6.93],
    [874921, 838912, 6750901.44, 1341376.16, 20.78, 12655, 14782, 16.14, 6.94],
    [945740, 876192, 6789438.77, 1427245.80, 21.31, 14406, 16897, 15.68, 7.06],
    [942662, 965432, 7598847.37, 1337729.25, 19.29, 14105, 17232, 14.98, 6.86],
    [812401, 854302, 6979081.49, 1305731.77, 21.21, 13219, 16698, 15.89, 6.76],
    [938402, 785302, 6587421.07, 1285501.19, 20.99, 12467, 15679, 16.97, 7.03],
    [1078522, 663329, 5248603.91, 1209289.66, 21.09, 11474, 12992, 17.57, 8.00],
    [843937, 865332, 7592743.02, 1397701.73, 21.34, 11409, 16308, 20.31, 8.45],
]

# meta realizado
allData10 = [
    [632520, 868095],
    [631000, 65572],
    [61430, 685964],
    [7400, 718304],
    [750, 708000],
    [7300, 69925],
    [754000, 727743],
    [768000, 708469],
    [770000, 691381],
    [750000, 717607],
    [62569, 66305],
    [789000, 76857],
]

allData11 = [
    [13185200, 764104],
    [578244, 936292],
    [894502, 842509],
    [764802, 915710],
    [951331, 868602],
    [874921, 838912],
    [945740, 876192],
    [942662, 965432],
    [812401, 854302],
    [938402, 785302],
    [1078522, 663329],
    [843937, 865332]
]
allData12 = [
    [4503, 764104],
    [5744, 936292],
    [8902, 842509],
    [7602, 915710],
    [9531, 868602],
    [8721, 838912],
    [9440, 876192],
    [9462, 965432],
    [8101, 854302],
    [93802, 785302],
    [107522, 663329],
    [84337, 865332]
]
allData13 = [
    [63250, 628095],
    [63100, 610572],
    [687830, 687964],
    [74790, 710304],
    [75790, 708000],
    [73400, 698925],
    [75120, 728743],
    [76430, 735469],
    [77000, 690381],
    [75030, 710607],
    [66040, 668305],
    [78930, 769857],
]

allData14 = [
    [13185200, 764104],
    [578244, 936292],
    [894502, 842509],
    [764802, 915710],
    [951331, 868602],
    [874921, 838912],
    [945740, 876192],
    [942662, 965432],
    [812401, 854302],
    [938402, 785302],
    [1078522, 663329],
    [843937, 865332],
]
allData15 = [
    [458903, 764104],
    [578244, 936292],
    [894502, 842509],
    [764802, 915710],
    [951331, 868602],
    [874921, 838912],
    [945740, 876192],
    [942662, 965432],
    [812401, 854302],
    [938402, 785302],
    [1078522, 663329],
    [843937, 865332],
]
allData16 = [
    [458903, 764104],
    [578244, 936292],
    [894502, 842509],
    [764802, 915710],
    [951331, 868602],
    [874921, 838912],
    [945740, 876192],
    [942662, 965432],
    [812401, 854302],
    [938402, 785302],
    [1078522, 663329],
    [843937, 865332],
]


vendas = "6.430.133"
entradas = "7.195,786"
percentual = "89%"

vendas2 = "5.800.000"
entradas2 = "6.500,000"
percentual2 = "88%"


evolucao = {
    # 2023 análise comercial
    "fat": "16,81%",
    "rent": "18,21%"
}

evolucao2 = {
    # 2022 análise comercial
    "fat": "16,81%",
    "rent": "18,21%"
}

evolucao3 = {
    # 2022 faturamento
    "fat": "-68,14%",
    "rent": "-67,78%"
}

evolucao4 = {
    # 2021 faturamento
    "fat": "-70,32%",
    "rent": "-69,94%"
}

evolucao5 = {
    # 2020 faturamento
    "fat": "-72,51%",
    "rent": "-71,89%"
}

evolucao6 = {
    # 2019 faturamento
    "fat": "-74,83%",
    "rent": "-74,09%"
}

evolucao7 = {
    # 2018 faturamento
    "fat": "-77,29%",
    "rent": "-76,44%"
}

evolucao8 = {
    # 2017 faturamento
    "fat": "-79,89%",
    "rent": "-78,92%"
}

evolucao9 = {
    # 2016 faturamento
    "fat": "-82,64%",
    "rent": "-81,56%"
}
soma = {
    # 2023 analise comercial
        "soma": "1917.118.127,25",
        "media1": "65.706.042,42",
        "media2": "13.043.724,32",
        "percentual": "19,85%",
        "valor1": "11,468",
        "valor2": "45.415.813,15",
        "valor3": "11.121.082,14",
        "valor4": "4.412.847,86",
        "valor5": "13.432"
    }
soma2 = {
    # 2022 analise comercial
    "soma": "1.815.120.111,78",
    "media1": "63.602.034,14",
    "media2": "12.877.243,89",
    "percentual": "18,78%",
    "valor1": "10,968",
    "valor2": "44.315.813,15",
    "valor3": "10.101.082,14",
    "valor4": "4.212.847,86",
    "valor5": "12.932"
}
soma3 = {
    # 2022 faturamento
    "soma": "38.148,87",
    "media1": "3.539.286,26",
    "media2": "706.373,85",
    "percentual": "19,96%"
}

soma4 = {
    # 2021 faturamento
    "soma": "35.836.159,77",
    "media1": "3.256.014,52",
    "media2": "651.203,90",
    "percentual": "18,92%"
}

soma5 = {
    # 2020 faturamento
    "soma": "32.745.123,69",
    "media1": "2.977.738,52",
    "media2": "595.547,70",
    "percentual": "17,86%"
}

soma6 = {
    # 2019 faturamento
    "soma": "29.670.112,59",
    "media1": "2.697.282,96",
    "media2": "539.456,59",
    "percentual": "16,80%"
}

soma7 = {
    # 2018 faturamento
    "soma": "26.603.107,49",
    "media1": "2.418.282,41",
    "media2": "483.656,48",
    "percentual": "15,74%"
}

soma8 = {
    # 2017 faturamento
    "soma": "23.542.102,39",
    "media1": "2.139.281,85",
    "media2": "427.856,37",
    "percentual": "14,68%"
}
soma9 = {
    # 2015 faturamento
    "soma": "20.486.097,29",
    "media1": "1.860.281,30",
    "media2": "372.056,26",
    "percentual": "13,62%"
}
@app.route('/')
def dashboard():
     
    

    return render_template('analisecomercial.html',
                           allData2=allData2,
                           allData=allData,
                           evolucao=evolucao, evolucao2=evolucao2,
                           soma=soma, soma2=soma2, vendas=vendas,
                           vendas2=vendas2, entradas=entradas, entradas2=entradas2,
                           percentual=percentual, percentual2=percentual2
                           )

@app.route('/analisecomercial')
def dashboard_a():

    return render_template('analisecomercial.html',
                           allData2=allData2,
                           allData=allData,
                           evolucao=evolucao, evolucao2=evolucao2,
                           soma=soma, soma2=soma2, vendas=vendas,
                           vendas2=vendas2, entradas=entradas, entradas2=entradas2,
                           percentual=percentual, percentual2=percentual2)



def matriz_para_lista(matriz):
    matriz_copia = np.copy(matriz)
    matriz_copia[:,0] = matriz_copia[:,0] / 1000
    matriz_copia[:,1] = matriz_copia[:,1] / 1000 
    matriz = matriz_copia
    lista = [[float("{:.2f}".format(item)) for item in row] for row in matriz]
    return lista

@app.route('/faturamento')
def faturamento():
    #ano = request.form['ano']
    ano = 2023
    anos = [str(ano - i) for i in range(1, 7)]
    #print(anos, ano)

    allData3 = gr.consulta('GERAL', 'GERAL', anos[0],1) #valor correspondente a 2022
    matriz = np.array(allData3)
    matrizr = matriz_para_lista(matriz)
    allData3 = matrizr
    print(allData3)

    soma_A10 = "{:,.2f}".format(np.sum(matriz[:,0]/1000))
    soma_A11 = "{:,.2f}".format(np.mean(matriz[:,0]/1000))
    soma_A12 = "{:,.2f}".format(np.mean(matriz[:,1]/1000))
    soma_A13 = "{:.2f}".format(np.mean(matriz[:,2]))
    #print(soma_A10, soma_A11, soma_A12, soma_A13)

    allData4 = gr.consulta('GERAL', 'GERAL', anos[1],1) #valor correspondente a 2021
    matriz = np.array(allData4)
    matrizr = matriz_para_lista(matriz)
    allData4 = matrizr
    print(allData4)

    matriz = np.array(allData4)
    soma_A21 = np.sum(matriz[:,0])
    soma_A22 = np.mean(matriz[:,1])
    media_A23 = np.mean(matriz[:,2])

    allData5 = gr.consulta('GERAL', 'GERAL', anos[2],1) #valor correspondente a 2020
    matriz = np.array(allData5)
    matrizr = matriz_para_lista(matriz)
    allData5 = matrizr
    print(allData5)

    matriz = np.array(allData5)
    soma_A31 = np.sum(matriz[:,0])
    soma_A32 = np.sum(matriz[:,1])
    media_A33 = np.mean(matriz[:,2])

    allData6 = gr.consulta('GERAL', 'GERAL', anos[3],1) #valor correspondente a 2019
    matriz = np.array(allData6)
    matrizr = matriz_para_lista(matriz)
    allData6 = matrizr
    print(allData6)   
    
    matriz = np.array(allData6)
    soma_A41 = np.sum(matriz[:,0])
    soma_A42 = np.sum(matriz[:,1])
    media_A43 = np.mean(matriz[:,2])

    allData7 = gr.consulta('GERAL', 'GERAL', anos[4],1) #valor correspondente a 2018
    matriz = np.array(allData7)
    matrizr = matriz_para_lista(matriz)
    allData7 = matrizr
    print(allData7)   

    matriz = np.array(allData7)
    soma_A51 = np.sum(matriz[:,0])
    soma_A52 = np.sum(matriz[:,1])
    media_A53 = np.mean(matriz[:,2])

    allData8 = gr.consulta('GERAL', 'GERAL', anos[5],1) #valor correspondente a 2017
    matriz = np.array(allData8)
    matrizr = matriz_para_lista(matriz)
    allData8 = matrizr
    print(allData8)   

    matriz = np.array(allData8)
    soma_A61 = np.sum(matriz[:,0])
    soma_A62 = np.sum(matriz[:,1])
    media_A63 = np.mean(matriz[:,2])

    allData9 = gr.consulta('GERAL', 'GERAL', '2016',1) #valor correspondente a 2016
    matriz = np.array(allData9)
    matrizr = matriz_para_lista(matriz)
    allData9 = matrizr
    print(allData9)   

    matriz = np.array(allData9)
    soma_A71 = np.sum(matriz[:,0])
    soma_A72 = np.sum(matriz[:,1])
    media_A73 = np.mean(matriz[:,2])

    return render_template('faturamento.html',
                           allData9=allData9,
                           allData8=allData8,
                           allData7=allData7,
                           allData6=allData6,                           
                           allData5=allData5,
                           allData4=allData4,
                           allData3=allData3,
                           evolucao3=evolucao3, evolucao4=evolucao4, evolucao5=evolucao5, 
                           evolucao6=evolucao6, evolucao7=evolucao7, evolucao8=evolucao8, 
                           evolucao9=evolucao9, soma3=soma3, soma4=soma4, soma5=soma5, 
                           soma6=soma6, soma7=soma7, soma8=soma8, soma9=soma9, anos=anos, soma_A10=soma_A10, soma_A11=soma_A11, soma_A12=soma_A12, soma_A13=soma_A13,)


@app.route('/metarealizado')
def metarealizado():
    return render_template('metarealizado.html',
                           allData16=allData16,
                           allData15=allData15,
                           allData14=allData14,
                           allData13=allData13,
                           allData12=allData12,
                           allData11=allData11,
                           allData10=allData10,
                           vendas=vendas, entradas=entradas, percentual=percentual,
                           evolucao=evolucao, vendas2=vendas2, entradas2=entradas2, percentual2=percentual2,
                           evolucao2=evolucao2, )



if __name__ == '__main__':
    app.run(debug=True)