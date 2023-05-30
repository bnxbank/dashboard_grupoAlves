#gera_csv.py
import pandas as pd
import numpy as np
import random
import string
from faker import Faker

# Gera datas aleatórias
start = pd.to_datetime('2023-01-01')
end = pd.to_datetime('2023-12-31')

def random_dates(start, end, n=10):
    start_u = start.value//10**9
    end_u = end.value//10**9
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')

# Gera nomes aleatórios
fake = Faker()
def random_names(n):
    return [fake.name() for _ in range(n)]

data = {
    #'Data': random_dates(start, end, 1000),
    'Valor': np.random.uniform(100, 500, 1000).round(2),
    'Consulta': np.random.uniform(60, 800, 1000).round(2),
}

df = pd.DataFrame(data)

# Converta o DataFrame em um array numpy
data = df.to_numpy()


# Salvamos o DataFrame como um arquivo CSV
#data.to_csv('atendimentos.csv', index=False)
np.savetxt('atendimentos.csv', data, delimiter=';', fmt='%s')

# Exibindo as primeiras linhas do DataFrame
print(df.head())
