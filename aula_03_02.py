# Programa média com desvio
nome = input("informe o seu nome: ")
n1 = float(input("informe sua Nota 1:"))
n2 = float(input("informe sua Nota 2:"))
media = (n1 + n2) / 2
if media >= 70:
    print(f"Sr.(a) {nome}, a sua média foi {media}, portanto você está Aprovado!")
elif media >= 30:
    print(f"Sr.(a) {nome}, a sua média foi {media}, portanto você está em recuperação")
else:
    print(f"Sr.(a) {nome}, você está Reprovado!")