import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Carregando o arquivo CSV
data_frame = pd.read_csv('base_vendas.csv')

data_frame['valor_total'] = data_frame ['qtd_vendida'] * data_frame['preco_unitario']

valor_total = data_frame['valor_total'].sum()
qnt_total = data_frame['valor_total'].count()
valor_total_medio = data_frame['valor_total'].mean()
valor_total_minimo = data_frame['valor_total'].min()
valor_total_maximo = data_frame['valor_total'].max()

print('Valor Total:', valor_total)
print('Valor Minimo:', valor_total_minimo)
print('Valor Medio:', valor_total_medio)
print('Valor Maximo:', valor_total_maximo)

filtro = data_frame[data_frame['preco_unitario'] > 2000]
filtro_total = (filtro.count())
print(filtro_total)

plt.hist(data_frame['valor_total'], bins=6, color='purple')
plt.xlabel('qtd_vendida')
plt.ylabel('Frequência')
plt.title('Distribuição de Valor Total')
plt.show()

data_frame['valor_usd'] = data_frame['valor_total'] / 5.70
print(data_frame.head())

preco_baixo = data_frame[data_frame['preco_unitario'] < 1000]
preco_medio = data_frame[(data_frame['preco_unitario'] >= 1000) & (data_frame['preco_unitario'] <=2000) ]
preco_acima = data_frame[data_frame['preco_unitario'] > 2000]

print(preco_baixo)
print(preco_medio)
print(preco_acima)