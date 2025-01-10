# Importando a Biblioteca Pandas e Numpy
import pandas as pd
import numpy as np

# Importando a Base de Dados 
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame funcionários
df_funcionarios = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')
