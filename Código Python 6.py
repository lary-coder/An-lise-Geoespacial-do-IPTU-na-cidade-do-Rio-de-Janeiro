import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
caminho_arquivo = "/content/drive/MyDrive/Python/IPTU+ITBI- Isenções_2018-2024.xlsx"

# Ler os dados da planilha Tabela4 do arquivo Excel
dados = pd.read_excel(caminho_arquivo, sheet_name="TabelaRA")

# Definir as colunas desejadas
colunas = ['Regiões Administrativas', 'Média de IPTU_Não residencial', 'Média de IPTU_Residencial', 'Média de IPTU_Territorial']

# Filtrar os dados para incluir apenas as colunas desejadas dados_filtrados = dados[colunas]

# Configurar o índice como 'Regiões Administrativas' dados_filtrados.set_index('Regiões Administrativas', inplace=True)

# Criar o gráfico de colunas dados_filtrados.plot(kind='bar', figsize=(10, 6))

# Adicionar título e rótulos aos eixos
plt.title('Média de IPTU por tipo e Região Administrativa') plt.xlabel('Regiões Administrativas')
plt.ylabel('Valor médio de IPTU')

# Mostrar o gráfico plt.show()
