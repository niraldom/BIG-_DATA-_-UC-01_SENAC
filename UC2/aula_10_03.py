import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_cvli = df_ocorrencias[['aisp','cvli']]
df_cvli = df_cvli.groupby(['aisp']).sum(['cvli']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_cvli.head())

# Criando o array dos cvli
array_cvli = np.array(df_cvli["cvli"])

# Obtendo a média dos cvli
media_cvli = np.mean(array_cvli)

# Obtendo a mediana dos cvli
mediana_cvli = np.median(array_cvli)

# Obtendo a distância entre a média e a mediana dos cvli
distancia_cvli = abs((media_cvli - mediana_cvli) / mediana_cvli) * 100

# Obtendo o máximo e o mínimo dos cvli
maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

# Obtendo a amplitude dos cvli
amplitude_cvli = maximo_cvli - minimo_cvli

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli

# Identificando os outliers superiores e inferiores dos cvli
limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

# Filtrando o DataFrame cvli
df_cvli_outliers_superiores = df_cvli[df_cvli['cvli'] > limite_superior_cvli]
df_cvli_outliers_inferiores = df_cvli[df_cvli['cvli'] < limite_inferior_cvli]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_cvli = np.var(array_cvli)
distancia_var_cvli = variancia_cvli / (media_cvli**2)

desvio_padrao_cvli = np.std(array_cvli)
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli


# Exibindo os dados sobre os cvli
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS CVLI -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos cvli é {media_cvli:.0f}")
print(f"A mediana dos cvli é {mediana_cvli:.0f}")
print(f"A distância entre a média e a mediana é dos cvli é {distancia_cvli:.2f} %")
print(f"O menor valor dos cvli é {minimo_cvli:.0f}")
print(f"O maior valor dos cvli é {maximo_cvli:.0f}")
print(f"A amplitude dos dos cvli é {amplitude_cvli:.0f}")
print(f"O valor do q1 - 25% dos cvli é {q1_cvli:.0f}")
print(f"O valor do q2 - 50% dos cvli é {q2_cvli:.0f}")
print(f"O valor do q3 - 75% dos cvli é {q3_cvli:.0f}")
print(f"O valor do iqr = q3 - q1 dos cvli é {iqr_cvli:.0f}")
print(f"O limite inferior dos cvli é {limite_inferior_cvli:.0f}")
print(f"O limite superior dos cvli é {limite_superior_cvli:.0f}")
print(f"A variância dos cvli é {variancia_cvli:.0f}")
print(f"A distância da variância X média dos cvli é {distancia_var_cvli:.0f}")
print(f"O desvio padrão dos cvli é {desvio_padrao_cvli:.0f}")
print(f"O coeficiente de variação dos cvli é {coeficiente_var_cvli:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_cvli_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_cvli_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_cvli_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_cvli_outliers_superiores)

# Visualizando os dados sobre os cvli
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre CVLI')

# posição 01: Gráfico dos cvli
plt.subplot(2,2,1)
plt.title('BoxPlot dos cvli')
plt.boxplot(array_cvli,vert=False,showmeans=True)

# posição 02: Histograma dos cvli
plt.subplot(2,2,2)
plt.title('Histograma dos cvli')
plt.hist(array_cvli,bins=100,edgecolor='black')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
plt.title('Ranking dos Batalhoes de PM com Outliers Superiores')
plt.barh(df_cvli_outliers_superiores_order['aisp'].astype(str),df_cvli_outliers_superiores_order['cvli'])


# posição 04: Medidas descritivas dos cvli
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos cvli')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos cvli {media_cvli:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos cvli {mediana_cvli:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos cvli {distancia_cvli:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor  dos cvli {maximo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos cvli {minimo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos cvli {distancia_var_cvli:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos cvli {coeficiente_var_cvli:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()