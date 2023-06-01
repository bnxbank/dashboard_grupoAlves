import psycopg2

cache = {}

def consulta(secao, loja, ano, sql1, cache=cache): 
    # Verifique se os resultados desta consulta já estão no cache
    cache_key = (secao, loja, ano, sql1)
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
    if sql1 == 1:
        cur.execute("SELECT SUM(f.valores) as valores_faturamento, SUM(r.valores) as valores_rentabilidade, SUM(rp.valores) as valores_rentabilidadeporcentagem, EXTRACT(YEAR FROM f.Datas) as ano, EXTRACT(MONTH FROM f.Datas) as mes  FROM  graficos_faturamento f JOIN graficos_rentabilidade r ON f.Datas = r.Datas AND f.Loja = r.Loja AND f.secao = r.secao JOIN graficos_rentabilidadeporcentagem rp ON f.Datas = rp.DATAS  AND f.Loja = rp.Loja AND f.secao = rp.secao WHERE f.Datas >= '"+ano+"-01-01' AND f.Datas <= '"+ano+"-12-31' AND f.secao = '"+secao+"' AND f.Loja = '"+loja+"'  GROUP BY  EXTRACT(YEAR FROM f.Datas), EXTRACT(MONTH FROM f.Datas) ORDER BY ano, mes")
        #cur.execute("SELECT COALESCE(f.valores, 0)::numeric as valores_faturamento, COALESCE(r.valores, 0)::numeric as valores_rentabilidade, COALESCE(rp.valores, 0)::numeric as valores_rentabilidadeporcentagem, EXTRACT(YEAR FROM f.Datas) as ano, EXTRACT(MONTH FROM f.Datas) as mes  FROM  graficos_faturamento f JOIN graficos_rentabilidade r ON f.Datas = r.Datas AND f.Loja = r.Loja AND f.secao = r.secao JOIN graficos_rentabilidadeporcentagem rp ON f.Datas = rp.DATAS  AND f.Loja = rp.Loja AND f.secao = rp.secao WHERE f.Datas >= '"+ano+"-01-01' AND f.Datas <= '"+ano+"-12-31' AND f.secao = '"+secao+"' AND f.Loja = '"+loja+"'  GROUP BY  EXTRACT(YEAR FROM f.Datas), EXTRACT(MONTH FROM f.Datas) ORDER BY ano, mes")
    if sql1 == 2:
        cur.execute("SELECT SUM(f.valores) as valores_faturamento, SUM(r.valores) as valores_rentabilidade, SUM(rp.valores) as valores_rentabilidadeporcentagem, EXTRACT(YEAR FROM f.datas) as ano, EXTRACT(MONTH FROM f.datas) as mes  FROM  graficos_estoque f JOIN graficos_rupturacompra r ON f.datas  = r.Datas AND f.Loja = r.Loja AND f.secao = r.secao JOIN graficos_rupturacompra rp ON f.datas  = rp.DATAS  AND f.Loja = rp.Loja AND f.secao = rp.secao WHERE f.datas >= '"+ano+"-01-01' AND f.datas  <= '"+ano+"-12-31' AND f.secao = '"+secao+"' AND f.Loja = '"+secao+"'  GROUP BY  EXTRACT(YEAR FROM f.datas),EXTRACT(MONTH FROM f.datas) ORDER BY ano, mes")
    if sql1 == 3:
        cur.execute("SELECT COALESCE(f.valores, 0)::numeric as vlrfaturamento, COALESCE(r.valores, 0)::numeric as vlrrentabilidade, COALESCE(rp.valores, 0)::numeric as vlrrentperc, COALESCE(iv.valores, 0)::numeric as vlritenvend, COALESCE(ie.valores, 0)::numeric as vlritenent, COALESCE(e.valores, 0)::numeric as vlrestoque,COALESCE(rc.valores, 0)::numeric as vlrrupcomp, COALESCE(es.valores, 0)::numeric as skuest, COALESCE(s.valores, 0)::numeric as skuvend FROM public.graficos_estoque e LEFT JOIN graficos_faturamento f ON f.loja = e.loja AND f.datas = e.datas AND f.secao = e.secao LEFT JOIN graficos_rentabilidade r ON r.loja = e.loja AND r.datas = e.datas AND r.secao = e.secao LEFT JOIN graficos_rentabilidadeporcentagem rp ON rp.loja = e.loja AND rp.datas = e.datas AND rp.secao = e.secao LEFT JOIN graficos_itensvendidos iv ON iv.loja = e.loja AND iv.datas   = e.datas AND iv.secao = e.secao LEFT JOIN graficos_itensdeentrada ie ON ie.loja = e.loja AND ie.datas   = e.datas AND ie.secao = e.secao LEFT JOIN graficos_rupturacompra rc ON rc.loja = e.loja AND rc.datas = e.datas AND rc.secao = e.secao LEFT JOIN graficos_skuestoque es ON es.loja = e.loja AND es.datas   = e.datas AND es.secao = e.secao LEFT JOIN graficos_sku s ON s.loja = e.loja AND s.datas  = e.datas AND s.secao = e.secao WHERE  e.loja = '"+loja+"'  AND e.secao = '"+secao+"' AND e.datas >= '"+ano+"-01-01' AND e.datas <= '"+ano+"-12-31'")



    # Recupere os resultados 
    rows = cur.fetchall()
    
    # create a list to hold the output data
    allData = []

    # iterate over the rows and add each one to the list
    for row in rows:
        if sql1 == 3:
            allData.append([float(val) if val is not None else 0.0 for val in row[:9]])
        else:
            allData.append([float(val) if val is not None else 0.0 for val in row[:3]])

    cache[cache_key] = allData
    #print(allData)
    # print the output data
    return allData


    # Feche o cursor e a conexão
    cur.close()
    con.close()

#print(consulta('GERAL', 'GERAL', '2020', 1))