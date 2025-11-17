# Análise descritiva import numpy as np
import scipy.stats as stats

# teste de normalidade Shapiro-Wilk
# Testar a normalidade de cada variável de IPTU
# shapiro_iptu_não residencial = stats.shapiro(dados['IPTU_Não Residencial'].dropna())
# shapiro_iptu_residencial = stats.shapiro(dados['IPTU_Residencial'].dropna()) # shapiro_iptu_territorial = stats.shapiro(dados['IPTU_Territorial'].dropna())

# Shapiro-Wilk test for normality shapiro_iptu_não_residencial = stats.shapiro(dados['Média de IPTU_Não residencial'].dropna())
shapiro_iptu_residencial = stats.shapiro(dados['Média de IPTU_Residencial'].dropna())
shapiro_iptu_territorial = stats.shapiro(dados['Média de IPTU_Territorial'].dropna())

# Print the test results print("Shapiro-Wilk test results:")
print(f"IPTU_Não Residencial: statistic =
{shapiro_iptu_não_residencial.statistic:.4f}, p-value =
{shapiro_iptu_não_residencial.pvalue:.4e}") print(f"IPTU_Residencial: statistic =
{shapiro_iptu_residencial.statistic:.4f}, p-value =
{shapiro_iptu_residencial.pvalue:.4e}") print(f"IPTU_Territorial: statistic =
{shapiro_iptu_territorial.statistic:.4f}, p-value =
{shapiro_iptu_territorial.pvalue:.4e}")
