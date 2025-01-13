import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'Bases\Financeira.csv'

# Criando o DataFrame financeira
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')
df_financeira_simples = df_financeira[['Id_cliente','Renda','Vlr_emprestado']]

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_financeira.head())
print('\n---- EXIBINDO A BASE DE DADOS SIMPLES -----')
print(df_financeira_simples.head())


# Criando o array da Renda e valores Emprestados
array_financeira_Renda = np.array(df_financeira["Renda"])
array_financira_Vlr_emprestado = np.array(df_financeira["Vlr_emprestado"])

# Obtendo a média do valor da Renda e Valor Emprestado
media_renda = np.mean(array_financeira_Renda)
media_vlr_emprestado = np.mean(array_financira_Vlr_emprestado)

# Obtendo a mediana do valor da Renda e Valor Emprestado
mediana_renda = np.median(array_financeira_Renda)
mediana_vlr_emprestado = np.median(array_financira_Vlr_emprestado)

# Obtendo a distância entre a média e a mediana do valor da renda e do vlr_emprestado
distancia_renda = abs((media_renda - mediana_renda) / mediana_renda)
distancia_vlr_emprestado = abs((media_vlr_emprestado - mediana_vlr_emprestado) / mediana_vlr_emprestado)

# Obtendo o máximo e o mínimo do valor da renda e do vlr_emprestado


# Obtendo a amplitude do valor da renda e do vlr_emprestado


# Obtendo os Quartis da renda e do vlr_emprestado - Método weibull




# Exibindo os dados sobre o valor das rendas
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS RENDAS --")
print(f"O Valor Médio das Rendas dos Clientes é {media_renda:.2f}")
print(f"O Valor da Mediana das Rendas dos Clientes é {mediana_renda:.2f}")




# Exibindo os dados sobre os valores emprestados