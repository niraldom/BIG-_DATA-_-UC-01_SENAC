import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_carga = df_ocorrencias[['munic','roubo_carga']]
df_roubo_carga = df_roubo_carga.groupby(['munic']).sum(['roubo_carga']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_roubo_carga.head())

# Criando o array de roubo de carga
array_roubo_carga = np.array(df_roubo_carga["roubo_carga"])

# Obtendo a média de roubo de carga
media_roubo_carga = np.mean(array_roubo_carga)

# Obtendo a mediana de roubo de carga
mediana_roubo_carga = np.median(array_roubo_carga)

# Obtendo a distância entre a média e a mediana de roubo de carga
distancia_roubo_carga = abs((media_roubo_carga - mediana_roubo_carga) / mediana_roubo_carga)

# Obtendo o máximo e o mínimo de roubo de carga
maximo_roubo_carga = np.max(array_roubo_carga)
minimo_roubo_carga = np.min(array_roubo_carga)

# Obtendo a amplitude de roubo de carga
amplitude_roubo_carga = maximo_roubo_carga - minimo_roubo_carga

# Obtendo os Quartis dos homicídios dolosos - Método weibull
q1_roubo_carga = np.quantile(array_roubo_carga, 0.25, method='weibull')
q2_roubo_carga = np.quantile(array_roubo_carga, 0.50, method='weibull')
q3_roubo_carga = np.quantile(array_roubo_carga, 0.75, method='weibull')
iqr_roubo_carga = q3_roubo_carga - q1_roubo_carga

# Identificando os outliers superiores e inferiores dos roubos de carga
limite_superior_roubo_carga = q3_roubo_carga + (1.5 * iqr_roubo_carga)
limite_inferior_roubo_carga = q1_roubo_carga - (1.5 * iqr_roubo_carga)

# Filtrando o DataFrame roubo de carga
df_roubo_carga_outliers_superiores = df_roubo_carga[df_roubo_carga['roubo_carga'] > limite_superior_roubo_carga]
df_roubo_carga_outliers_inferiores = df_roubo_carga[df_roubo_carga['roubo_carga'] < limite_inferior_roubo_carga]




# Exibindo os dados sobre os homicídios dolosos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS HOMICÍDIOS DOLOSOS -----------")
print(f"A média de roubos de carga é {media_roubo_carga:.0f}")
print(f"A mediana de roubos de carga é {mediana_roubo_carga:.0f}")
print(f"A distância entre a média e a mediana de roubo de carga é {distancia_roubo_carga}")
print(f"O menor valor dos roubos de carga é {minimo_roubo_carga:.0f}")
print(f"O maior valor dos roubos de carga é {maximo_roubo_carga:.0f}")
print(f"A amplitude dos valores dos roubo_carga é {amplitude_roubo_carga:.0f}")
print(f"O valor do q1 - 25% dos roubo_carga é {q1_roubo_carga:.0f}")
print(f"O valor do q2 - 50% dos roubo_carga é {q2_roubo_carga:.0f}")
print(f"O valor do q3 - 75% dos roubo_carga é {q3_roubo_carga:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubo de carga é {iqr_roubo_carga:.0f}")
print(f"O limite inferior dos roubo de carga é {limite_inferior_roubo_carga:.0f}")
print(f"O limite superior dos roubo de carga é {limite_superior_roubo_carga:.0f}")
print(f"O limite inferior dos roubo de carga é {limite_inferior_roubo_carga:.0f}")
print(f"O limite superior dos roubo de carga é {limite_superior_roubo_carga:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_carga_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_carga_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_carga_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_carga_outliers_superiores)