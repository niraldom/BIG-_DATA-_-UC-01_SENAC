import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Lessão Corporal Dolosa
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_les_dolo = df_ocorrencias[['cisp','ano','lesao_corp_dolosa']]
# Criando o DataFrame Lessão Corporal Dolosa agrupado pelos anos de 2022, 2023 e 2024
df_les_dolo = df_les_dolo[df_les_dolo['ano'].isin([2022,2023,2024])]
df_les_dolo = df_les_dolo.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index()


# Criando o DataFrame Lessão Corporal Culposa
df_les_culp = df_ocorrencias[['cisp','ano','lesao_corp_culposa']]
# Criando o DataFrame Lessão Corporal Culposa agrupado pelos anos de 2022, 2023 e 2024
df_les_culp = df_les_culp[df_les_culp['ano'].isin([2022,2023,2024])]
df_les_culp = df_les_culp.groupby(['cisp']).sum(['lesao_corp_culposa']).reset_index()


# Criando o DataFrame Lessão Corporal Dolosa e Culposa
df_les_dolo_culp = df_ocorrencias[['cisp','lesao_corp_dolosa','lesao_corp_culposa']]
df_les_dolo_culp = df_les_dolo_culp.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_culposa']).reset_index()



# Exibindo a base de dados Lessão Corporal Dolosa
print('\n---- EXIBINDO A BASE DE DADOS Lessão Corporal Dolosa -----')
print(df_les_dolo.head())


# Exibindo a base de dados Lessão Corporal Dolosa e Culposa
print('\n---- EXIBINDO A BASE DE DADOS Lessão Corporal Dolosa e Culposa-----')
print(df_les_dolo_culp.head())

# Criando o array da Lesão Corporal Dolosa
array_les_dolo = np.array(df_les_dolo["lesao_corp_dolosa"])

# Obtendo a média da Lesão Corporal Dolosa
media_les_dolo = np.mean(array_les_dolo)

# Obtendo a mediana da Lesão Corporal Dolosa
mediana_les_dolo = np.median(array_les_dolo)

# Obtendo a distância entre a média e a mediana da Lesão Corporal Dolosa
distancia_les_dolo = abs((media_les_dolo - mediana_les_dolo) / mediana_les_dolo) * 100

# Obtendo o máximo e o mínimo da Lesão Corporal Dolosa
maximo_les_dolo = np.max(array_les_dolo)
minimo_les_dolo = np.min(array_les_dolo)

# Obtendo a amplitude da Lesão Corporal Dolosa
amplitude_les_dolo = maximo_les_dolo - minimo_les_dolo

# Obtendo os Quartis da Lesão Corporal Dolosa - Método weibull
q1_les_dolo = np.quantile(array_les_dolo, 0.25, method='weibull')
q2_les_dolo = np.quantile(array_les_dolo, 0.50, method='weibull')
q3_les_dolo = np.quantile(array_les_dolo, 0.75, method='weibull')
iqr_les_dolo = q3_les_dolo - q1_les_dolo

# Identificando os outliers superiores e inferiores da Lesão Corporal Dolosa
limite_superior_les_dolo = q3_les_dolo + (1.5 * iqr_les_dolo)
limite_inferior_les_dolo = q1_les_dolo - (1.5 * iqr_les_dolo)

# Filtrando o DataFrame da Lesão Corporal Dolosa
df_les_dolo_outliers_superiores = df_les_dolo[df_les_dolo['lesao_corp_dolosa'] > limite_superior_les_dolo]
df_les_dolo_outliers_inferiores = df_les_dolo[df_les_dolo['lesao_corp_dolosa'] < limite_inferior_les_dolo]

# Obtendo as medidas de dispersão da Lesão Corporal Dolosa
variancia_les_dolo = np.var(array_les_dolo)
distancia_var_les_dolo = variancia_les_dolo / (media_les_dolo**2)

desvio_padrao_les_dolo = np.std(array_les_dolo)
coeficiente_var_les_dolo = desvio_padrao_les_dolo / media_les_dolo


# Criando o array da Lesão Corporal Culposa
array_les_culposa = np.array(df_les_culp["lesao_corp_culposa"])

# Obtendo a média da Lesão Corporal Culposa
media_les_Culposa = np.mean(array_les_culposa)

# Obtendo a mediana da Lesão Corporal Culposa
mediana_les_Culposa = np.median(array_les_culposa)

# Obtendo a distância entre a média e a mediana da Lesão Corporal Culposa
distancia_les_Culposa = abs((media_les_Culposa - mediana_les_Culposa) / mediana_les_Culposa) * 100

# Obtendo o máximo e o mínimo da Lesão Corporal Culposa
maximo_les_Culposa = np.max(array_les_culposa)
minimo_les_Culposa = np.min(array_les_culposa)

# Obtendo a amplitude da Lesão Corporal Culposa
amplitude_les_Culposa = maximo_les_Culposa - minimo_les_Culposa

# Obtendo os Quartis da Lesão Corporal Culposa - Método weibull
q1_les_Culposa = np.quantile(array_les_culposa, 0.25, method='weibull')
q2_les_Culposa = np.quantile(array_les_culposa, 0.50, method='weibull')
q3_les_Culposa = np.quantile(array_les_culposa, 0.75, method='weibull')
iqr_les_Culposa = q3_les_Culposa - q1_les_Culposa

# Identificando os outliers superiores e inferiores da Lesão Corporal Culposa
limite_superior_les_Culposa = q3_les_Culposa + (1.5 * iqr_les_Culposa)
limite_inferior_les_Culposa = q1_les_Culposa - (1.5 * iqr_les_Culposa)

# Filtrando o DataFrame da Lesão Corporal Culposa
df_les_Culposa_outliers_superiores = df_les_culp[df_les_culp['lesao_corp_culposa'] > limite_superior_les_Culposa]
df_les_Culposa_outliers_inferiores = df_les_culp[df_les_culp['lesao_corp_culposa'] < limite_inferior_les_Culposa]

# Obtendo as medidas de dispersão da Lesão Corporal Culposa
variancia_les_Culposa = np.var(array_les_culposa)
distancia_var_les_Culposa = variancia_les_Culposa / (media_les_Culposa**2)

desvio_padrao_les_Culposa = np.std(array_les_culposa)
coeficiente_var_les_Culposa = desvio_padrao_les_Culposa / media_les_Culposa

# Obtendo a correlação entre as recuperações e os roubos de veículos
# 0.9 a 1.0 (positivo ou negativo) - muito forte
# 0.7 a 0.9 (positivo ou negativo) - forte
# 0.5 a 0.7 (positivo ou negativo) - moderada
# 0.3 a 0.5 (positivo ou negativo) - fraca
# 0.0 a 0.3 (positivo ou negativo) - não possui correlação
correl_les_dolo_culposa = np.corrcoef(df_les_dolo_culp['lesao_corp_dolosa'],df_les_dolo_culp['lesao_corp_culposa'])[0,1]


# Exibindo os dados sobre Lessão Corporal Dolosa
print("\n--------- OBTENDO INFORMAÇÕES SOBRE LESSÃO CORPORAL DOLOSA  -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média de Lessão Corporal Dolosa é {media_les_dolo:.0f}")
print(f"A mediana de Lessão Corporal Dolosa é {mediana_les_dolo:.0f}")
print(f"A distância entre a média e a mediana de Lessão Corporal Dolosa é {distancia_les_dolo:.2f} %")
print(f"O menor valor de Lessão Corporal Dolosa é {minimo_les_dolo:.0f}")
print(f"O maior valor de Lessão Corporal Dolosa é {maximo_les_dolo:.0f}")
print(f"A amplitude dos valores de Lessão Corporal Dolosa é {amplitude_les_dolo:.0f}")
print(f"O valor do q1 - 25% de Lessão Corporal Dolosa é {q1_les_dolo:.0f}")
print(f"O valor do q2 - 50% de Lessão Corporal Dolosa é {q2_les_dolo:.0f}")
print(f"O valor do q3 - 75% de Lessão Corporal Dolosa é {q3_les_dolo:.0f}")
print(f"O valor do iqr = q3 - q1 de Lessão Corporal Dolosa é {iqr_les_dolo:.0f}")
print(f"O limite inferior de Lessão Corporal Dolosa é {limite_inferior_les_dolo:.0f}")
print(f"O limite superior de Lessão Corporal Dolosa é {limite_superior_les_dolo:.0f}")
print(f"A variância de Lessão Corporal Dolosa é {variancia_les_dolo:.0f}")
print(f"A distância da variância X média de Lessão Corporal Dolosa é {distancia_les_dolo:.0f}")
print(f"O desvio padrão de Lessão Corporal Dolosa é {desvio_padrao_les_dolo:.0f}")
print(f"O coeficiente de variação de Lessão Corporal Dolosa é {coeficiente_var_les_dolo:.0f}")
print(f"A correlação entre Lessão Corporal Dolosa e Culposa é {correl_les_dolo_culposa:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_les_dolo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_les_dolo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_les_dolo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_les_dolo_outliers_superiores)

# Exibindo os dados sobre Lessão Corporal Culposa
print("\n--------- OBTENDO INFORMAÇÕES SOBRE LESSÃO CORPORAL CULPOSA  -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média de Lessão Corporal Culposa é {media_les_Culposa:.0f}")
print(f"A mediana de Lessão Corporal Culposa é {mediana_les_Culposa:.0f}")
print(f"A distância entre a média e a mediana de Lessão Corporal Culposa é {distancia_les_Culposa:.2f} %")
print(f"O menor valor de Lessão Corporal Culposa é {minimo_les_Culposa:.0f}")
print(f"O maior valor de Lessão Corporal Culposaa é {maximo_les_Culposa:.0f}")
print(f"A amplitude dos valores de Lessão Corporal Culposa é {amplitude_les_Culposa:.0f}")
print(f"O valor do q1 - 25% de Lessão Corporal Culposa é {q1_les_Culposa:.0f}")
print(f"O valor do q2 - 50% de Lessão Corporal  Culposa é {q2_les_Culposa:.0f}")
print(f"O valor do q3 - 75% de Lessão Corporal Culposa é {q3_les_Culposa:.0f}")
print(f"O valor do iqr = q3 - q1 de Lessão Corporal Culposa é {iqr_les_Culposa:.0f}")
print(f"O limite inferior de Lessão Corporal Culposa é {limite_inferior_les_Culposa:.0f}")
print(f"O limite superior de Lessão Corporal Culposa é {limite_superior_les_Culposa:.0f}")
print(f"A variância de Lessão Corporal Culposa é {variancia_les_Culposa:.0f}")
print(f"A distância da variância X média de Lessão Corporal Culposa é {distancia_les_Culposa:.0f}")
print(f"O desvio padrão de Lessão Corporal Culposa é {desvio_padrao_les_Culposa:.0f}")
print(f"O coeficiente de variação de Lessão Corporal Culposa é {coeficiente_var_les_Culposa:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_les_Culposa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_les_Culposa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_les_Culposa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_les_Culposa_outliers_superiores)    

# Visualizando os dados sobre Lessões Corporais
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,3,figsize=(23,8))
plt.suptitle('Análise dos Dados sobre Lessões Corporais',fontsize=16)

# posição 01: BoxPlot das Lessões Corporais Dolosas
plt.subplot(2,3,1)
plt.title('BoxPlot das Lessões Corporais Dolosas')
plt.boxplot(array_les_dolo,vert=False,showmeans=True)

# posição 02: Ranking das DP´s com Outliers Superiores
plt.subplot(2,3,2)
df_les_dolo_outliers_superiores_order = df_les_dolo_outliers_superiores.sort_values(by='lesao_corp_dolosa',ascending=True)
plt.title('Ranking das DPs com Outliers Superiores')
plt.barh(df_les_dolo_outliers_superiores_order['cisp'].astype(str),df_les_dolo_outliers_superiores_order['lesao_corp_dolosa'])

# posição 03: Histograma das Lessões Corporais Dolosas
plt.subplot(2,3,3)
plt.title('Histograma das Lessões Corporais Dolosas')
plt.hist(array_les_dolo,bins=100,edgecolor='black')

# posição 04: Correlação entre as Lessões Corporais Dolosas e Culposas
plt.subplot(2,3,4)
plt.title('Comparativo das Lessões Corporais Dolosas e Culpoas')
plt.scatter(df_les_dolo_culp['lesao_corp_dolosa'],df_les_dolo_culp['lesao_corp_culposa'])
plt.xlabel('lesao_corp_dolosa')
plt.ylabel('lesao_corp_culposa')

# posição 05: Medidas descritivas das Recuperações de Veículos
plt.subplot(2,3,5)
plt.title('Medidas Descritivas das Lessões Corporais Dolosas')
plt.axis('off')
plt.text(0.0,0.9,f'Média das Lessões Corporais dolosas  {media_les_dolo:.0f}',fontsize=12)
plt.text(0.0,0.8,f'Mediana das Lessões Corporais dolosas {mediana_les_dolo:.0f}',fontsize=12)
plt.text(0.0,0.7,f'Distância entre Média e Mediana das Lessões Corporais dolosas {distancia_les_dolo:.2f}%',fontsize=12)
plt.text(0.0,0.6,f'Maior valor das Lessões Corporais dolosas {maximo_les_dolo:.0f}',fontsize=12)
plt.text(0.0,0.5,f'Menor valor das Lessões Corporais dolosas {minimo_les_dolo:.0f}',fontsize=12)
plt.text(0.0,0.4,f'Distância entre a Variância e Média das Lessões Corporais dolosas {distancia_var_les_dolo:.2f}',fontsize=12)
plt.text(0.0,0.3,f'Coeficiente de variação das Lessões Corporais dolosas {coeficiente_var_les_dolo:.2f}',fontsize=12)

# posição 06: Medidas descritivas das Lessões Corporais Culposas
plt.subplot(2,3,6)
plt.title('Medidas Descritivas das Lessões Corporais Culposas')
plt.axis('off')
plt.text(0.0,0.9,f'Média das Lessões Corporais Culposas {media_les_Culposa:.0f}',fontsize=12)
plt.text(0.0,0.8,f'Mediana das Lessões Corporais Culposas {mediana_les_Culposa:.0f}',fontsize=12)
plt.text(0.0,0.7,f'Distância entre Média e Mediana das Lessões Corporais Culposas {distancia_les_Culposa:.2f}%',fontsize=12)
plt.text(0.0,0.6,f'Maior valor das Lessões Corporais Culposas {maximo_les_Culposa:.0f}',fontsize=12)
plt.text(0.0,0.5,f'Menor valor das Lessões Corporais Culposas {minimo_les_Culposa:.0f}',fontsize=12)
plt.text(0.0,0.4,f'Distância entre a Variância e Média das Lessões Corporais Culposas {distancia_var_les_Culposa:.2f}',fontsize=12)
plt.text(0.0,0.3,f'Coeficiente de variação das Lessões Corporais Culposas {coeficiente_var_les_Culposa:.2f}',fontsize=12)


# Exibindo o Painel
plt.tight_layout()
plt.show()