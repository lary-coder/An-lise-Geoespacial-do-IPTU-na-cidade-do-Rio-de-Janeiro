import pandas as pd

# Carrega todas as planilhas do arquivo em um dicionário planilhas = pd.read_excel(
"/content/drive/MyDrive/Python/IPTU 2023 imóveis Rio de Janeiro.xlsx",
sheet_name=None,
)

# Concatena as planilhas verticalmente
df_concat = pd.concat(planilhas.values(), ignore_index=True)

# Salva a planilha concatenada df_concat.to_excel("iptu_2023_imoveis_rj_convertido.xlsx", index=False)

print("Planilhas concatenadas com sucesso!")
