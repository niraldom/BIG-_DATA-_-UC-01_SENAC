# Programa para tratar erros de divisão
while True:
    try:
        n1 = int(input("Informe o primeiro valor: "))
        n2 = int(input("Informe o segurdo valor: "))
        r = (n1 / n2)
    except ZeroDivisionError:
        print("Verifique o segundo valor digitado, pois ele não pode ser zero")
    else:
        print(f"o resultado da divisão é: {r}")
        break
