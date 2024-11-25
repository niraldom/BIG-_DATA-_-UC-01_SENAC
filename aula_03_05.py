# Programa doador de sangue
idade = int(input("informe a sua idade "))
peso = float(input("informe o seu peso em kg "))
sono = float(input("informe quantas horas dormiu na última noite "))
if (idade >=16 and idade <=69) and (peso >= 50) and (sono >= 6):
    print("Parabéns, você está apto a doar sangue ")
else:
    print("Infelizmente você não está apto a doar sangue ")
