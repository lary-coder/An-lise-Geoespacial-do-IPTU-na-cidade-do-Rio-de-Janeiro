import pandas as pd

import matplotlib.pyplot as plt import seaborn as sns
import geopandas as gpd import pandas as pd

# Caminho do arquivo Excel
caminho_arquivo = "/content/drive/MyDrive/Python/IPTU+ITBI- Isenções_2018-2024.xlsx"

# Ler os dados da planilha Tabela4 do arquivo Excel
dados = pd.read_excel(caminho_arquivo, sheet_name="TabelaRA") dados.shape
dados.info()

#média de cada tipo de iptu por ra
round(dados['Média de IPTU_Não residencial'].mean(), 2)

#média de cada tipo de iptu por ra round(dados['Média de IPTU_Residencial'].mean(), 2)

#média de cada tipo de iptu por ra round(dados['Média de IPTU_Territorial'].mean(), 2)

# medidas descritivas round(dados.describe(), 2)
