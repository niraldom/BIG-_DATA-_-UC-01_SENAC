# programa que realiza soma de 5 números inteiros e fornece o maior valor
soma = 0
maior = 0
for i in range(5):
    num = int(input("informe o valor: "))
    if num > maior:
        maior = num
    soma = soma + num
print(f"O resultado da soma é: {soma}")
print(f"O maior valor informado é: {maior}")
