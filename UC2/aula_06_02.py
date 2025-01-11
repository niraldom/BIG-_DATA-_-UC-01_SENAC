import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'BASES\Titanic.csv'

# Criando o DataFrame financeira
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_titanic_simples = df_titanic[['Name','Sex','Age','Fare']]

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_titanic.head())
print('\n---- EXIBINDO A BASE DE DADOS SIMPLES -----')
print(df_titanic_simples.head())

# Criando o array do valor da passagem e da idade
array_titanic_fare = np.array(df_titanic["Fare"])
array_titanic_age = np.array(df_titanic["Age"])

# Obtendo a média do valor da passagem e da idade
media_fare = np.mean(array_titanic_fare)
media_age = np.mean(array_titanic_age)

# Obtendo a mediana do valor da passagem e da idade
mediana_fare = np.median(array_titanic_fare)
mediana_age = np.median(array_titanic_age)

# Obtendo a distância entre a média e a mediana do valor da passagem e da idade
distancia_fare = abs((media_fare - mediana_fare) / mediana_fare)
distancia_age = abs((media_age - mediana_age) / mediana_age)

# Obtendo o máximo e o mínimo do valor da passagem e da idade
maximo_fare = np.max(array_titanic_fare)
maximo_age = np.max(array_titanic_age)
minimo_fare = np.min(array_titanic_fare)
minimo_age = np.min(array_titanic_age)

# Obtendo a amplitude do valor da passagem e da idade
amplitude_fare = maximo_fare - minimo_fare
amplitude_age = maximo_age - minimo_age

# Obtendo os limites superiores e inferiores da passagen
q1_passagem = np.quantile(array_titanic_fare, 0.25, method='weibull')
q2_passagem = np.quantile(array_titanic_fare, 0.50, method='weibull')
q3_passagem = np.quantile(array_titanic_fare, 0.75, method='weibull')
iqr_passagem = q3_passagem - q1_passagem
limite_superior_passagem = q3_passagem + (1.5 * iqr_passagem)
limite_inferior_passagem = q1_passagem - (1.5 * iqr_passagem)
df_titanic_outliers_inferiores_passagem = df_titanic[df_titanic['Fare'] < limite_inferior_passagem]
df_titanic_outliers_superiores_passagem = df_titanic[df_titanic['Fare'] > limite_superior_passagem]

# Obtendo os limites superiores e inferiores da idade
q1_idade = np.quantile(array_titanic_age, 0.25, method='weibull')
q2_idade = np.quantile(array_titanic_age, 0.50, method='weibull')
q3_idade = np.quantile(array_titanic_age, 0.75, method='weibull')
iqr_idade = q3_idade - q1_idade
limite_superior_idade = q3_idade + (1.5 * iqr_idade)
limite_inferior_idade = q1_idade - (1.5 * iqr_idade)
df_titanic_outliers_inferiores_idade = df_titanic[df_titanic['Age'] < limite_inferior_idade]
df_titanic_outliers_superiores_idade = df_titanic[df_titanic['Age'] > limite_superior_idade]
#nome_func_novo = df_funcionarios[df_funcionarios['Idade'] == menor_idade]['Nome']
#nome_func_antigo = df_funcionarios[df_funcionarios['Idade'] == maior_idade]['Nome']


# Exibindo os dados sobre o valor das passagens
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS PASSAGENS --")
print('Medidas de Tendência Central')
print(f"\nA média das passagens é {media_fare:.2f}")
print(f"A mediana das passagens é {mediana_fare:.2f}")
print(f"A distância entre a média e a mediana é {distancia_fare}")
print(f"O menor valor das passagens é {minimo_fare:.2f}")
print(f"O maior valor das passagens é {maximo_fare:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_fare:.2f}")
print(f"O valor do quartil 1 é {q1_passagem}")
print(f"O valor do quartil 2 é {q2_passagem}")
print(f"O valor do quartil 3 é {q3_passagem}")
print(f"O valor do iqr é {iqr_passagem}")
print(f"O limite inferior é {limite_inferior_passagem}")
print(f"O limite superior é {limite_superior_passagem}")
if len(df_titanic_outliers_inferiores_passagem) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_titanic_outliers_inferiores_passagem)
if len(df_titanic_outliers_superiores_passagem) == 0:
    print("Não existem outliers superiores")
else:
    print(df_titanic_outliers_superiores_passagem)

# Exibindo os dados sobre as idades dos passageiros
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS IDADES --")
print('Medidas de Tendência Central')
print(f"\nA média das idades é {media_age:.1f}")
print(f"A mediana das idades é {mediana_age:.1f}")
print(f"A distância entre a média e a mediana é {distancia_age}")
print(f"O menor valor das idades é {minimo_age}")
print(f"O maior valor das idades é {maximo_age}")
print(f"A amplitude dos valores das idades é {amplitude_age}")