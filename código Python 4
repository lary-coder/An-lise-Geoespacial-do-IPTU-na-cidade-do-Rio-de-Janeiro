import pandas as pd

# Carregar a planilha df =
pd.read_excel('/content/drive/MyDrive/Python/PlanilhaIPTU_PGV_Censo RJ.xlsx', sheet_name='Valores_teste')

# Contar o número total de células para cada Bairro total = df.groupby('Bairro').size()

# Contar o número de células nulas e não nulas para cada Bairro nulos = df['VALOR'].isnull().groupby(df['Bairro']).sum() nao_nulos = total - nulos

# Calcular o percentual de células nulas e não nulas para cada Bairro
percentual_nulos = (nulos / total) * 100 percentual_nao_nulos = (nao_nulos / total) * 100

# Criar uma nova planilha com as colunas Bairro e percentual novo_df = pd.DataFrame({
'Bairro': total.index,
'Percentual de Nulos': percentual_nulos, 'Percentual de Não Nulos': percentual_nao_nulos
})

# Salvar a nova planilha novo_df.to_excel('/content/drive/MyDrive/Python/Novo_PlanilhaIPTU_P GV_CensoRJ.xlsx', index=False)
