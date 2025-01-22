import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_ocorrencias[['cisp','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_roubo_veiculo.head())

# Criando o array de roubo de veiculo
array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])

# Obtendo a média de roubo de veiculo
media_roubo_veiculo = np.mean(array_roubo_veiculo)

# Obtendo a mediana de roubo de veiculo
mediana_roubo_veiculo = np.median(array_roubo_veiculo)

# Obtendo a distância entre a média e a mediana de roubo de veiculo
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)

# Obtendo o máximo e o mínimo de roubo de veiculo
maximo_roubo_veiculo = np.max(array_roubo_veiculo)
minimo_roubo_veiculo = np.min(array_roubo_veiculo)

# Obtendo a amplitude de roubo de veiculo
amplitude_roubo_veiculo = maximo_roubo_veiculo - minimo_roubo_veiculo

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

# Identificando os outliers superiores e inferiores dos roubos de veiculos
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)

# Filtrando o DataFrame roubo de veiculo
df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior_roubo_veiculo]




# Exibindo os dados sobre roubo de veículos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE ROUBO DE VEÍCULOS -----------")
print(f"A média de roubos de veículos é {media_roubo_veiculo:.0f}")
print(f"A mediana de roubos de veículos  é {mediana_roubo_veiculo:.0f}")
print(f"A distância entre a média e a mediana de roubo de veículos é {distancia_roubo_veiculo}")
print(f"O menor valor dos roubos de veículos é {minimo_roubo_veiculo:.0f}")
print(f"O maior valor dos roubos de veículos é {maximo_roubo_veiculo:.0f}")
print(f"A amplitude dos valores dos roubo_veículos é {amplitude_roubo_veiculo:.0f}")
print(f"O valor do q1 - 25% dos roubo_veículos é {q1_roubo_veiculo:.0f}")
print(f"O valor do q2 - 50% dos roubo_veículos é {q2_roubo_veiculo:.0f}")
print(f"O valor do q3 - 75% dos roubo_veículos é {q3_roubo_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubo de veículos é {iqr_roubo_veiculo:.0f}")
print(f"O limite inferior dos roubo de veículos é {limite_inferior_roubo_veiculo:.0f}")
print(f"O limite superior dos roubo de veículos é {limite_superior_roubo_veiculo:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_veiculo_outliers_superiores)

    # Visualizando os dados sobre roubos de veículos
print("\nVISUALIZANDO OS DADOS...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre os Roubos de Veículos por delegacias')

if len(df_roubo_veiculo_outliers_superiores) != 0 or len(df_roubo_veiculo_outliers_inferiores) != 0:
    # Posição 01: Gráfico dos roubo de veículos
    plt.subplot(2,2,1)
    plt.title('BoxPlot dos roubos de veículos')
    plt.boxplot(array_roubo_veiculo,vert=False,showmeans=True)

    # Posição 02: Histograma dos roubo de veículos
    plt.subplot(2,2,2)
    plt.title('Histograma dos roubos de veículos')
    plt.hist(array_roubo_veiculo,bins=100,edgecolor='black')

    # Posição 03: Lista de Delegacias com Outliers
    df_roubo_veiculo_outliers_superiores_order = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
    plt.subplot(2,2,3)
    plt.title('Ranking das Delegacias com Outliers Superiores')

    plt.barh(df_roubo_veiculo_outliers_superiores_order['cisp'],df_roubo_veiculo_outliers_superiores_order['roubo_veiculo'])

# Posição 04: Medidas Descritivas dos roubos de veículos
    plt.subplot(2,2,4)
    plt.title('Medidas Descritivas dos roubos de veiculos')
    plt.axis('off')
    plt.text(0.1,0.9,f'A média dos roubos de veículos é {media_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'A mediana dos roubos de veículos é {mediana_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'A distância entre a média e a mediana é dos roubos de veículos é {distancia_roubo_veiculo}',fontsize=12)
    plt.text(0.1,0.6,f'O menor valor dos roubos de veículos é {minimo_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'O maior valor dos roubos de veículos é {maximo_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'A amplitude dos valores dos roubos de veículos é {amplitude_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.3,f'O valor do q3 - 75% dos roubos de veículos é {q3_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.2,f'O valor do iqr = q3 - q1 dos roubos de veículos é {iqr_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.1,f'O limite superior dos roubos de veículos é {limite_superior_roubo_veiculo:.0f}',fontsize=12)
else:

    # Posição 01: Gráfico dos roubos de veículos
    df_roubo_veiculo_order = df_roubo_veiculo.sort_values(by='roubo_veiculo',ascending=True)
    plt.subplot(2,2,1)
    plt.xticks([])
    plt.title('Acumulado dos Valores dos Roubos de Veículos')

    plt.bar(df_roubo_veiculo_order['cisp'].astype(str),df_roubo_veiculo_order['roubo_veiculo'])

    # Posição 02: Histograma dos roubos de veículos
    plt.subplot(2,2,2)
    plt.title('Histograma dos roubos de veículos')
    plt.hist(array_roubo_veiculo,bins=100,edgecolor='black')

    # Posição 03: Medidas Descritivas dos roubos de veículos
    plt.subplot(2,2,3)
    plt.title('Medidas Descritivas dos roubos de veículos')
    plt.axis('off')
    plt.text(0.1,0.9,f'A média dos roubos de veículos é {media_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.8,f'A mediana dos roubos de veículos é {mediana_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.7,f'A distância entre a média e a mediana é dos roubos de veículos é {distancia_roubo_veiculo}',fontsize=12)
    plt.text(0.1,0.6,f'O menor valor dos roubos de veículos é {minimo_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.5,f'O maior valor dos roubos de veículos é {maximo_roubo_veiculo:.0f}',fontsize=12)
    plt.text(0.1,0.4,f'A amplitude dos valores dos roubos de veículos é {amplitude_roubo_veiculo:.0f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
