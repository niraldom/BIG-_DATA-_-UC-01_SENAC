# Programa para determinar a quantidade de valores pares e impares
qtd_par = 0
qtd_impar = 0
numeros = [10, 15, 12, 13, 11, 21, 22, 50, 30, 45]
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        qtd_par += 1
    else:
        qtd_impar += 1
print(f"A quantidade de númreos pares é: {qtd_par}")
print(f"A quantidade de números impares é: {qtd_impar}")
print("ordem de criação")
print(numeros)
print("ordem Reversa")
numeros.reverse()
print(numeros)
print("ordem crescente")
numeros.sort()
print(numeros)