# Importando a Biblioteca
import pandas as pd

# importando a Base de Dados
endereco_dados = 'BASES\Finaceira.csv'

# Criando o DataFrame Financeira
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Exibindo o DataFrame
print(df_financeira.head())