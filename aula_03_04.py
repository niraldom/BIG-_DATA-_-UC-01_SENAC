# Programa igual ou diferente
n1 = int(input("informe um número inteiro:"))
n2 = int(input("informe um número inteiro:"))
s = n1 + n2
p = n1 * n2
if n1 == n2:
    print(f"os números informados são iguais e seu produto é {p}")
else:
    print(f"os números informados são diferentes e sua soma é {s}")