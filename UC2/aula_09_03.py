import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_recuperacao_veiculos = df_ocorrencias[['aisp','recuperacao_veiculos']]
df_recuperacao_veiculos = df_recuperacao_veiculos.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_recuperacao_veiculos.head())

# Criando o array de recuperação de veículos
array_recuperacao_veiculos = np.array(df_recuperacao_veiculos["recuperacao_veiculos"])

# Obtendo a média de recuperação de veículos
media_recuperacao_veiculos = np.mean(array_recuperacao_veiculos)

# Obtendo a mediana de recuperação de veículos
mediana_recuperacao_veiculos = np.median(array_recuperacao_veiculos)

# Obtendo a distância entre a média e a mediana de recuperação de veículos
distancia_recuperacao_veiculos = abs((media_recuperacao_veiculos - mediana_recuperacao_veiculos) / mediana_recuperacao_veiculos)

# Obtendo o máximo e o mínimo de recuperação de veículos
maximo_recuperacao_veiculos = np.max(array_recuperacao_veiculos)
minimo_recuperacao_veiculos = np.min(array_recuperacao_veiculos)

# Obtendo a amplitude de recuperação de veículos
amplitude_recuperacao_veiculos = maximo_recuperacao_veiculos - minimo_recuperacao_veiculos

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.25, method='weibull')
q2_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.50, method='weibull')
q3_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.75, method='weibull')
iqr_recuperacao_veiculos = q3_recuperacao_veiculos - q1_recuperacao_veiculos

# Identificando os outliers superiores e inferiores dos recuperação de veículos
limite_superior_recuperacao_veiculos = q3_recuperacao_veiculos + (1.5 * iqr_recuperacao_veiculos)
limite_inferior_recuperacao_veiculos = q1_recuperacao_veiculos - (1.5 * iqr_recuperacao_veiculos)

# Filtrando o DataFrame recuperação de veículos
df_recuperacao_veiculos_outliers_superiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] > limite_superior_recuperacao_veiculos]
df_recuperacao_veiculos_outliers_inferiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculos]




# Exibindo os dados sobre roubo de veículos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE ROUBO DE VEÍCULOS -----------")
print(f"A média de recuperação de veículos é {media_roubo_veiculo:.0f}")
print(f"A mediana de recuperação de veículos  é {mediana_roubo_veiculo:.0f}")
print(f"A distância entre a média e a mediana de recuperação de veículos é {distancia_roubo_veiculo}")
print(f"O menor valor dos recuperação de veículos é {minimo_roubo_veiculo:.0f}")
print(f"O maior valor dos recuperação de veículos é {maximo_roubo_veiculo:.0f}")
print(f"A amplitude dos valores dos rrecuperação de veículos é {amplitude_roubo_veiculo:.0f}")
print(f"O valor do q1 - 25% de recuperação de veículos é {q1_roubo_veiculo:.0f}")
print(f"O valor do q2 - 50% de recuperação de veículos é {q2_roubo_veiculo:.0f}")
print(f"O valor do q3 - 75% de recuperação de veículos é {q3_roubo_veiculo:.0f}")
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
