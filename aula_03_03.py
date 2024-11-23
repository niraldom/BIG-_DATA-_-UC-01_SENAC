# Programa com desvio e conectivo
nome = input("informe o seu nome:")
sexo = input("informe o seu sexo (M OU F):")
idade = int(input("informe sua idade:"))
if (idade >= 18) and (sexo == "M" or sexo == "m"):
    certificado = int(input("informe o certificado de reservista:"))
elif idade >= 18:
    print("você é maior de idade")
else:
    print("você é menor de idade")