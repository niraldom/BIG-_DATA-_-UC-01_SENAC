# Importando a Biblioteca
import pandas as pd

# Criando as Séries
maria = pd.Series([800,700,1000,900,1200,600,600])
joao = pd.Series([900,500,1100,1000,900,500,700])
manoel = pd.Series([700,600,900,1200,900,700,400])

# Criando as Visualizações
print("------- Vendedora Maria -------")
print(f"O Total de Vendas foi: {maria.sum()}")
print(f"A Média de Vendas foi: {maria.mean():.2f}")
print(f"O Maior Valor Vendido foi: {maria.max()}")
print(f"O Menor Valor Vendido foi: {maria.min()}")

print("\n------- Vendedor João -------")
print(f"O Total de Vendas foi: {joao.sum()}")
print(f"A Média de Vendas foi: {joao.mean():.2f}")
print(f"O Maior Valor Vendido foi: {joao.max()}")
print(f"O Menor Valor Vendido foi: {joao.min()}")

print("\n------- Vendedor Manoel -------")
print(f"O Total de Vendas foi: {manoel.sum()}")
print(f"A Média de Vendas foi: {manoel.mean():.2f}")
print(f"O Maior Valor Vendido foi: {manoel.max()}")
print(f"O Menor Valor Vendido foi: {manoel.min()}")