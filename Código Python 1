# Importando a biblioteca pandas import pandas as pd

# Criando uma lista vazia para armazenar as planilhas planilhas = []

# Iterando de 1 a 700 (701 é exclusivo) para ler cada planilha for i in range(1, 701):

# Lendo cada planilha e armazenando em uma variável 'planilha' planilha = pd.read_excel('/content/drive/MyDrive/Python/PGV 2018 - 2017-06-12 COM Bairros.xlsx', sheet_name=f'Sheet{i}')

# Adicionando a planilha atual à lista de planilhas planilhas.append(planilha)

# Concatenando todas as planilhas da lista em um único DataFrame df_total = pd.concat(planilhas, ignore_index=True)

# Salvando o DataFrame total em um arquivo Excel df_total.to_excel('PGV2018total.xlsx')
