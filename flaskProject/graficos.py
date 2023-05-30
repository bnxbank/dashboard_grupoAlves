import psycopg2

cache = {}

def consulta(secao, loja, data_inicial, data_final): 
    # Verifique se os resultados desta consulta já estão no cache
    cache_key = (secao, loja, data_inicial, data_final)
    if cache_key in cache:
        return cache[cache_key]  
    # Conecte-se ao seu banco de dados
    con = psycopg2.connect(
                user="admin",
                password="postgress",
                host="204.12.240.157",
                port="5432",
                database="postgres"
    )

    # Crie um cursor
    cur = con.cursor()

    # Execute a consulta
    cur.execute("SELECT SUM(f.valores) as valores_faturamento, SUM(r.valores) as valores_rentabilidade, SUM(rp.valores) as valores_rentabilidadeporcentagem, EXTRACT(YEAR FROM f.Datas) as ano, EXTRACT(MONTH FROM f.Datas) as mes  FROM  graficos_faturamento f JOIN graficos_rentabilidade r ON f.Datas = r.Datas AND f.Loja = r.Loja AND f.secao = r.secao JOIN graficos_rentabilidadeporcentagem rp ON f.Datas = rp.""data""  AND f.Loja = rp.Loja AND f.secao = rp.secao WHERE f.Datas >= '"+data_inicial+"' AND f.Datas <= '"+data_final+"' AND f.secao = '"+secao+"' AND f.Loja = '"+loja+"'  GROUP BY  EXTRACT(YEAR FROM f.Datas), EXTRACT(MONTH FROM f.Datas) ORDER BY ano, mes")
    
    #print(cur.query)

    # Recupere os resultados
    rows = cur.fetchall()
    
    # create a list to hold the output data
    allData = []

    # iterate over the rows and add each one to the list
    for row in rows:
        allData.append([float(val) for val in row[:3]])

    cache[cache_key] = allData
    print(allData)
    # print the output data
    return allData


    # Feche o cursor e a conexão
    cur.close()
    con.close()

print(consulta('GERAL', 'GERAL', '2016-01-01', '2016-12-31'))