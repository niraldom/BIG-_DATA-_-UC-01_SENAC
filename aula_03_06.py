# maior número
n1 = int(input("informe o primeiro número inteiro:"))
n2 = int(input("informe o segundo número inteiro:"))
n3 = int(input("informe o terceiro número inteiro:"))
if (n1>n2) and (n1>n3):
    print(f"o maior número é {n1}")
elif (n2>n1) and (n2>n3):
    print(f"o maior número é {n2}")
else:
    print(f"o maior número é {n3}")
