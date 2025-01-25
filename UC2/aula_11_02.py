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
print(df_les_corp_dolo.head())


# Exibindo a base de dados Lessão Corporal Dolosa e Culposa
print('\n---- EXIBINDO A BASE DE DADOS Lessão Corporal Dolosa e Culposa-----')
print(df_rec_roubo_veiculo.head())