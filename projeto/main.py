from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Gerando dados fictícios
'''
np.random.seed(0)
datas = pd.date_range(start='2023-01-01', periods=100)
categorias = ['Eletrônicos', 'Roupas', 'Alimentos']
dados = {
    'Data': np.random.choice(datas, 100),
    'Categoria': np.random.choice(categorias, 100),
    'Vendas': np.random.randint(50, 500, 100)
}
'''
arquivo_csv = pd.read_csv('base_vendas.csv')

datas = []
categoria = []
vendas = []

for venda in arquivo_csv.itertuples():
    datas.append(venda.data)
    categoria.append(venda.produto)
    vendas.append(venda.qtd_vendida * venda.preco_unitario)
    
       
dados = {
    'Data': datas,
    'Categorias': categoria,
    'Vendas': vendas
}
        
        

# Inicializando o aplicativo Dash
app = Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    html.H1('Dashboard de Vendas'),
    dcc.DatePickerRange(
        id='date-picker',
        start_date=df['Data'].min(),
        end_date=df['Data'].max(),
        display_format='YYYY-MM-DD'
    ),
    dcc.Dropdown(
        id='categoria-dropdown',
        options=[{'label': cat, 'value': cat} for cat in categoria],
        value=categorias,  # Seleciona todas as categorias por padrão
        multi=True,
        placeholder="Selecione a(s) categoria(s)"
    ),
    dcc.Graph(id='grafico-vendas')
])
# Callback para atualizar o gráfico com base nos filtros
@app.callback(
    Output('grafico-vendas', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('categoria-dropdown', 'value')]
)
def atualizar_grafico(start_date, end_date, categorias_selecionadas):
 # Filtra os dados
    df_filtrado = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]
    df_filtrado = df_filtrado[df_filtrado['Categoria'].isin(categorias_selecionadas)]

# Cria o gráfico com Plotly
    fig = px.line(df_filtrado, x='Data', y='Vendas', color='Categoria', title='Vendas por Categoria')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)