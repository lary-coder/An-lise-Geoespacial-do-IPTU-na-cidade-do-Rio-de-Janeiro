import pandas as pd import json
from unidecode import unidecode import plotly.express as px

# Lendo o arquivo Excel file_path =
'/content/drive/MyDrive/Python/PlanilhaIPTU_PGV_CensoRJrev2.xlsx' df = pd.read_excel(file_path, sheet_name='TabelaRA')

# Selecionando apenas as colunas necessárias (Regiões Administrativas e Média de IPTU_Territorial)
df_iptu = df[['Regiões Administrativas', 'Média de IPTU_Territorial']]

# Função para normalizar os nomes (remover acentos e converter para minúsculas)
def normalize_name(name):
name = unidecode(name).lower()
name = name.replace("santa tereza", "santa teresa") #
Substituição manual return name

# Normalizando os nomes das regiões administrativas no DataFrame df_iptu['Regiões Administrativas'] = df_iptu['Regiões Administrativas'].apply(normalize_name)

# Carregando o arquivo GeoJSON geojson_path =
'/content/drive/MyDrive/Python/LimiteRA_RJ.geojson.json' with open(geojson_path, 'r') as f:
geo_uf = json.load(f)

# Normalizando os nomes das regiões administrativas no GeoJSON for feature in geo_uf['features']:
feature['properties']['nomera'] = normalize_name(feature['properties']['nomera'])

# Obtendo os valores mínimo e máximo de Média de IPTU_Territorial min_iptu = df_iptu['Média de IPTU_Territorial'].min()
max_iptu = df_iptu['Média de IPTU_Territorial'].max()

# Criando o mapa coroplético fig = px.choropleth_mapbox(
df_iptu, geojson=geo_uf,
locations='Regiões Administrativas', featureidkey='properties.nomera', color='Média de IPTU_Territorial', color_continuous_scale="Turbo", range_color=(min_iptu, max_iptu), mapbox_style='open-street-map',
zoom=10, # Ajuste para um nível de zoom apropriado labels={'Média de IPTU_Territorial': 'IPTU Médio Territorial
(R$)', 'nomera': 'Região Administrativa'}, center={"lat": -22.908333, "lon": -43.196388},
title='Mapa IPTU Territorial por RA', width=1000,
height=450
)

# Atualiza o layout
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Mostra o gráfico fig.show()
