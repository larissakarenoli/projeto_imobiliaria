# -*- coding: utf-8 -*-
"""projeto_imobiliaria.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l6XfXbs9fozrVrIKVT2t8o3Ths4JrO99

# Conhecendo a base de dados

## Importando os dados
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)

pd.read_csv(url, sep=';')

dados = pd.read_csv(url, sep=';')
dados

dados.head(10)

dados.tail()

type(dados)

"""## Características gerais da base de dados"""

dados.shape

dados.columns

dados.info()

dados['Tipo']

dados[['Quartos', 'Valor']]

"""# Análise exploratória de dados

## Qual o valor médio de aluguel por tipo de imóvel?
"""

dados.head()

dados['Valor'].mean()

dados.groupby('Tipo').mean(numeric_only=True)

dados.groupby('Tipo')['Valor'].mean()

dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind='barh', figsize=(14, 10), color = 'green');

"""## Removendo os imóveis comerciais"""

dados.Tipo.unique()

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio','Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

dados.query('@imoveis_comerciais in Tipo')

dados.query('@imoveis_comerciais not in Tipo')

df = dados.query('@imoveis_comerciais not in Tipo')
df.head()

df.Tipo.unique()

df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind='barh', figsize=(14, 10), color = 'blue');

"""## Qual o percentual de cada tipo de imóvel na nossa base de dados?"""

df.Tipo.unique()

df.Tipo.value_counts(normalize=True)

df.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color ='purple', xlabel = 'Tipos', ylabel = 'Percentual');



"""### **Selecionando apenas os imóveis do tipo apartamento**"""

df.query('Tipo == "Apartamento"')

df = df.query('Tipo == "Apartamento"')
df.head()

"""# Tratando e filtrando os dados

## Lidando com dados nulos
"""

df.isnull()

df.isnull().sum()

df.fillna(0)

df = df.fillna(0)

df.isnull().sum()



"""## Removendo registros"""

df.query('Valor == 0 | Condominio == 0')

df.query('Valor == 0 | Condominio == 0').index

registros_a_remover = df.query('Valor == 0 | Condominio == 0').index

df.drop(registros_a_remover, axis=0, inplace=True)

df.query('Valor == 0 | Condominio == 0')

df.head()

df.Tipo.unique()

df.drop('Tipo', axis=1, inplace=True)

df.head()

"""## Filtros

### **1. Apartamentos que possuem `1 quarto` e `aluguel menor que 1200`**
"""

df['Quartos'] == 1

selecao1 = df['Quartos'] == 1
df[selecao1]

selecao2 = df['Valor'] < 1200
df[selecao2]

selecao_final = (selecao1) & (selecao2)
df[selecao_final]

df_1 = df[selecao_final]

"""### **2. `Apartamentos` que possuem pelo menos `2 quartos`, `aluguel menor que 3000` e `area maior que 70`**"""

selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
df[selecao]

df_2 = df[selecao]

"""## Salvando os dados"""

df.to_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv', index=False)

pd.read_csv('dados_apartamentos.csv')

df.to_csv('dados_apartamentos.csv', index=False, sep=';')

pd.read_csv('dados_apartamentos.csv')

pd.read_csv('dados_apartamentos.csv', sep=';')



"""# Manipulando os dados

## Criando colunas numéricas
"""

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')
dados.head()

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados.head()

dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']
dados.head()

"""## Criando colunas categóricas"""

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']
dados.head()

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
dados['Quartos'] + ' quarto(s) ' + ' e ' + dados['Vagas'] + ' vaga(s) de garagem. '

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                     dados['Quartos'].astype(str) + ' quarto(s) ' + \
                     ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem. '
dados.head()

dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
dados.head()

dados.to_csv('dados_completos_dev.csv', index=False, sep=';')

