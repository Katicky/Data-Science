import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
data = {
    'Produto': [
        'Brombril', 
        'Ype', 
        'Esponja'],
    'Preço': [
        23.90,
        35.90,
        29.90
    ],
    'Cidade': [
        'São Paulo',
        'Rio de Janeiro',
        'Curítíba'
  ]
}

dataframe_Lista = pd.DataFrame(data)


plt.bar (data['Produto'],data ['Preço'], color='black')
plt.xlabel('Produtos')
plt.ylabel('Preços')
plt.title('Preços por Produto')
plt.show()
'''
'''
dados = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Vendas': [150, 200, 300, 100],
    'Custo': [100, 150, 200, 80],
    'Margem (%)': [0.33, 0.25, 0.5, 0.2]
}

#print(df.describe()) Para saber mais sobre o DataFrame


# Acrecimo de coluna
df = pd.DataFrame(dados)
df['Lucro'] = df['Vendas'] - df['Custo']
produto_maior_lucro = df.loc[df['Lucro'].idxmax()]
produto_maior_lucro = df.loc[df['Lucro'].idxmin()]
# Para selecionar um filtro é necessario mexer no ''idxmax''. Ou seja ''idxmax'' ou ''idxmin''.


plt.bar (df['Produto'],df ['Custo'], color='black')
plt.xlabel('Produto')
plt.ylabel('Custo')
plt.title('Preços por Produto')
plt.show()

print(produto_maior_lucro)
'''
'''
dados = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Vendas': [150, 200, 300, 100],
    'Custo': [100, 150, 200, 80],
    'Margem (%)': [0.33, 0.25, 0.5, 0.2]
}
# Acrecimo de coluna
df = pd.DataFrame(dados)
df['Lucro'] = df['Vendas'] - df['Custo']

media = np.mean(df['Margem (%)'])
print(media)
'''
dados = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Vendas': [150, 200, 300, 100],
    'Custo': [100, 150, 200, 80],
    'Margem (%)': [0.33, 0.25, 0.5, 0.2]
}
df = pd.DataFrame(dados)

plt.pie(df['Vendas'], labels=df['Produto'], autopct='%1.1f%%')
plt.show()



