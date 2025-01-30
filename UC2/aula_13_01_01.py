import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_comercio = df_ocorrencias[['cisp','roubo_comercio']]
df_roubo_comercio = df_roubo_comercio.groupby(['cisp']).sum(['roubo_comercio']).reset_index()

# Criando o DataFrame roubo de comércio e roubo de residências
df_roubo_comercio_residencia = df_ocorrencias[['cisp','roubo_comercio','roubo_residencia']]
df_roubo_comercio_residencia = df_roubo_comercio_residencia.groupby(['cisp']).sum(['roubo_comercio','roubo_residencia']).reset_index()

# Exibindo a base de dados roubo comércio
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_roubo_comercio.head())

# Criando o array roubo comércio
array_roubo_comercio = np.array(df_roubo_comercio["roubo_comercio"])

# Obtendo a média dos roubo comércio
media_roubo_comercio = np.mean(array_roubo_comercio)

# Obtendo a mediana dos roubo comércio
mediana_roubo_comercio = np.median(array_roubo_comercio)

# Obtendo a distância entre a média e a mediana dos roubo comércio
distancia_roubo_comercio = abs((media_roubo_comercio - mediana_roubo_comercio) / mediana_roubo_comercio)

# Obtendo o máximo e o mínimo dos roubo comércio
maximo_roubo_comercio = np.max(array_roubo_comercio)
minimo_roubo_comercio = np.min(array_roubo_comercio)

# Obtendo a amplitude dos roubo comércio
amplitude_roubo_comercio = maximo_roubo_comercio - minimo_roubo_comercio

# Obtendo os Quartis dos roubo comércio - Método weibull
q1_roubo_comercio = np.quantile(array_roubo_comercio, 0.25, method='weibull')
q2_roubo_comercio = np.quantile(array_roubo_comercio, 0.50, method='weibull')
q3_roubo_comercio = np.quantile(array_roubo_comercio, 0.75, method='weibull')
iqr_roubo_comercio = q3_roubo_comercio - q1_roubo_comercio

# Identificando os outliers superiores e inferiores dos roubo comércio
limite_superior_roubo_comercio = q3_roubo_comercio + (1.5 * iqr_roubo_comercio)
limite_inferior_roubo_comercio = q1_roubo_comercio - (1.5 * iqr_roubo_comercio)

# Filtrando o DataFrame roubo comércio
df_roubo_comercio_outliers_superiores = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] > limite_superior_roubo_comercio]
df_roubo_comercio_outliers_inferiores = df_roubo_comercio[df_roubo_comercio['roubo_comercio'] < limite_inferior_roubo_comercio]

# Obtendo as medidas de dispersão dos roubos de Comércio
variancia_roubo_comercio = np.var(array_roubo_comercio)
distancia_var_roubo_comercio = variancia_roubo_comercio / (media_roubo_comercio**2)

desvio_padrao_roubo_comercio = np.std(array_roubo_comercio)
coeficiente_var_roubo_comercio = desvio_padrao_roubo_comercio / media_roubo_comercio

# Obtendo a correlação entre roubo comércio e roubo residências
# 0.9 a 1.0 (positivo ou negativo) - muito forte
# 0.7 a 0.9 (positivo ou negativo) - forte
# 0.5 a 0.7 (positivo ou negativo) - moderada
# 0.3 a 0.5 (positivo ou negativo) - fraca
# 0.0 a 0.3 (positivo ou negativo) - não possui correlação
correl_roubo_comercio_residencia = np.corrcoef(df_roubo_comercio_residencia['roubo_comercio'],df_roubo_comercio_residencia['roubo_residencia'])[0,1]


# Exibindo os dados sobre os roubo comércio
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS ROUBO COMÉRCIO -----------")
print(f"A média dos roubos de comércio é {media_roubo_comercio:.0f}")
print(f"A mediana dos roubos de comércio é {mediana_roubo_comercio:.0f}")
print(f"A distância entre a média e a mediana é dos roubos de comércio é {distancia_roubo_comercio}")
print(f"O menor valor dos roubos de comércio é {minimo_roubo_comercio:.0f}")
print(f"O maior valor dos roubos de comércio é {maximo_roubo_comercio:.0f}")
print(f"A amplitude dos valores dos roubos de comércio é {amplitude_roubo_comercio:.0f}")
print(f"O valor do q1 - 25% dos roubos de comércio é {q1_roubo_comercio:.0f}")
print(f"O valor do q2 - 50% dos roubos de comércio é {q2_roubo_comercio:.0f}")
print(f"O valor do q3 - 75% dos roubos de comércio é {q3_roubo_comercio:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubos de comércio é {iqr_roubo_comercio:.0f}")
print(f"O limite inferior dos roubos de comércio é {limite_inferior_roubo_comercio:.0f}")
print(f"O limite superior dos roubos de ccomércio é {limite_superior_roubo_comercio:.0f}")
print(f"A variância dos roubos de comércio é {variancia_roubo_comercio:.0f}")
print(f"A distância da variância X média dos roubos de comércio é {distancia_var_roubo_comercio:.0f}")
print(f"O desvio padrão dos roubos de comércio é {desvio_padrao_roubo_comercio:.0f}")
print(f"O coeficiente de variação dos roubos de comércio é {coeficiente_var_roubo_comercio:.0f}")
print(f"A correlação entre o roubo de comércio e roubo de residência é {correl_roubo_comercio_residencia:.1f}")

if len(df_roubo_comercio_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_comercio_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_comercio_outliers_superiores) == 0:
    print("Não existem outliers superiores")
    controle_roubo_comercio = 0 
else:
    print(df_roubo_comercio_outliers_superiores)
    controle_roubo_comercio = 1 


    # Visualizando os dados sobre roubos de comércio
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(3,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre roubo de comércio')

# posição 01: BoxPlot dos roubos de comércio
plt.subplot(3,2,1)
plt.title('BoxPlot dos roubos de comércio')
plt.boxplot(array_roubo_comercio,vert=False,showmeans=True)

# posição 02: Dispersão entre os roubos de comércio
plt.subplot(3,2,2)
plt.title('Comparativo dos roubos de comércio e roubo de residência')
plt.scatter(df_roubo_comercio_residencia['roubo_comercio'],df_roubo_comercio_residencia['roubo_residencia'])
plt.xlabel('Roubos de Comércio')
plt.ylabel('Roubos de Residências')

# posição 03: 
plt.subplot(3,2,3)
if controle_roubo_comercio == 0:
    # Não possui outliers - exibindo os dados completos
    # para colocar apenas as 5 coloca .head(), para colocar se colocar um
    df_roubo_comercio_order = df_roubo_comercio.sort_values(by='roubo_comercio',ascending=True).head()
    plt.title('Ranking das Delegacias')
    plt.barh(df_roubo_comercio_order['cisp'].astype(str),df_roubo_comercio_order['roubo_comercio'])
else:
    # Possui outliers - exibindo apenas os dados discrepantes
    df_roubo_comercio_outliers_superiores_order = df_roubo_comercio_outliers_superiores.sort_values(by='roubo_comercio',ascending=True)
    plt.title('Ranking das Delegacias com Outliers')
    plt.barh(df_roubo_comercio_outliers_superiores_order['cisp'].astype(str),df_roubo_comercio_outliers_superiores_order['roubo_comercio'])

# posição 04:
plt.subplot(3,2,4)
df_roubo_comercio_order = df_roubo_comercio.sort_values(by='roubo_comercio',ascending=True)
df_roubo = df_roubo_comercio_order.head()
plt.title('Top 5 das Delegacias com Menores Valores')
plt.barh(df_roubo['cisp'].astype(str),df_roubo['roubo_comercio'])

# posição 05:
plt.subplot(3,2,5)
plt.title('Histograma dos roubos comercio')
plt.hist(array_roubo_comercio,bins=100,edgecolor='black')

# posição 06: Medidas descritivas das Lesões Corporais Dolosas
plt.subplot(3,2,6)
plt.title('Medidas Descritivas das Lesões Corporais Dolosas')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos roubos de comércio é: {media_roubo_comercio:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana Média dos roubos de comércio é: {mediana_roubo_comercio:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana Média dos roubos de comércio é: {distancia_roubo_comercio:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dMédia dos roubos de comércio é: {maximo_roubo_comercio:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor Média dos roubos de comércio é: {minimo_roubo_comercio:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média Média dos roubos de comércio é: {distancia_var_roubo_comercio:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação Média dos roubos de comércio é: {coeficiente_var_roubo_comercio:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação dos roubos de comércio e de residências é: {correl_roubo_comercio_residencia:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()