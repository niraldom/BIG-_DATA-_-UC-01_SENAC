import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados BaseDPEvolucaoMensalCisp
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv'

# criando o DataFrame Homicídio Doloso
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_doloso = df_ocorrencias[['upp','hom_doloso']]
# DataFrame Consolidado
df_hom_doloso = df_hom_doloso.groupby(['upp']).sum(['hom_doloso']).reset_index()

# Criando o array do Homicídio doloso
array_hom_doloso = np.array(df_hom_doloso["hom_doloso"])

# Obtendo os dados Homicídio doloso
media_hom_doloso = np.mean(array_hom_doloso)
mediana_hom_doloso = np.median(array_hom_doloso)
distancia = abs((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso) * 100
maximo = np.max(array_hom_doloso)
minimo = np.min(array_hom_doloso)
amplitude = maximo - minimo




# Exibindo a base de dados Delegacias - Roubo de Veículos
print('\n--- EXIBINDO A BASE E DADOS ---')
print(df_ocorrencias.head())
print('\n--- EXIBINDO A BASE E DADOS Roubo de Veículos ---')
print(df_hom_doloso.head())


