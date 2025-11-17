import pandas as pd
import json
from unidecode import unidecode import plotly.express as px

# Lendo o arquivo Excel file_path =
'/content/drive/MyDrive/Python/PlanilhaIPTU_PGV_CensoRJrev3.xlsx' df = pd.read_excel(file_path, sheet_name='TabelaRArev1')

# Selecionando apenas as colunas necessárias (Região_Adm e % Variação populacional)
df_iptu = df[['Região_Adm', '% Variação populacional']]

# Função para normalizar os nomes (remover acentos e converter para minúsculas)
def normalize_name(name):
name = unidecode(name).lower()
name = name.replace("santa tereza", "santa teresa") #
Substituição manual return name

# Normalizando os nomes das Região_Adm no DataFrame df_iptu['Região_Adm'] = df_iptu['Região_Adm'].apply(normalize_name)

# Convertendo a variação populacional para percentual df_iptu['% Variação populacional'] = df_iptu['% Variação populacional'] * 100

# Carregando o arquivo GeoJSON geojson_path =
'/content/drive/MyDrive/Python/LimiteRA_RJ.geojson.json' with open(geojson_path, 'r') as f:
geo_uf = json.load(f)

# Normalizando os nomes das regiões administrativas no GeoJSON for feature in geo_uf['features']:
feature['properties']['nomera'] = normalize_name(feature['properties']['nomera'])

# Obtendo os valores mínimo e máximo de % Variação populacional min_iptu = df_iptu['% Variação populacional'].min()
max_iptu = df_iptu['% Variação populacional'].max()

# Criando o mapa coroplético fig = px.choropleth_mapbox(
df_iptu, geojson=geo_uf, locations='Região_Adm',
featureidkey='properties.nomera', color='% Variação populacional', color_continuous_scale="Viridis",
range_color=(min_iptu, max_iptu), mapbox_style='open-street-map',
zoom=10, # Ajuste para um nível de zoom apropriado labels={'% Variação populacional': '% Variação populacional',
'nomera': 'Região_Adm'},
center={"lat": -22.908333, "lon": -43.196388},
title='Mapa % Variação populacional por RA', width=1000,
height=450
)

# Atualiza o layout
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Mostra o gráfico fig.show()

