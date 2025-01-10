# importando a Biblioteca Pandas
import pandas as pd

# Importando a Base de Dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Ocorrências
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Criando o DataFrame Homicídio Doloso por Município
df_hom_doloso_munic = df_ocorrencias[['munic','hom_doloso']]

# Consolidando o DataFrame HOmicídio Doloso por Município
df_hom_doloso_munic = df_hom_doloso_munic.groupby(['munic']).sum(['hom_doloso']).reset_index()


# Exibindo o DataFrame
print(df_ocorrencias.head())

#