# Importando a Biblioteca Pandas e Numpy
import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados Titanic.csv
endereco_dados = 'BASES\Titanic.csv'

# Criando o DataFrame Titanic
df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

# Exibindo a base de dados Titanic
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_titanic.head())

# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
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


# Exibindo os dados sobre o valor das passagens
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS PASSAGENS --")
print('Medidas de Tendência Central')
print(f"\nA média das passagens é {media_fare:.2f}")
print(f"A mediana das passagens é {mediana_fare:.2f}")
print(f"A distância entre a média e a mediana é {distancia_fare}")
print(f"O menor valor das passagens é {minimo_fare:.2f}")
print(f"O maior valor das passagens é {maximo_fare:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_fare:.2f}")


# Exibindo os dados sobre as idades dos passageiros
print("\n-- OBTENDO INFORMAÇÕES SOBRE AS IDADES --")
print('Medidas de Tendência Central')
print(f"\nA média das idades é {media_age:.1f}")
print(f"A mediana das idades é {mediana_age:.1f}")
print(f"A distância entre a média e a mediana é {distancia_age}")
print(f"O menor valor das idades é {minimo_age}")
print(f"O maior valor das idades é {maximo_age}")
print(f"A amplitude dos valores das idades é {amplitude_age}")
