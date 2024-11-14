# Prestação em atraso
prestacao = float(input("informe o valor da prestação: "))
taxa = float(input("informe a taxa mensal: "))
tempo = float(input("informe a quantidade de meses em atraso: "))
valor_final = prestacao+(prestacao*(taxa/100)*tempo)
print(f"O valor final da prestação é R$ {valor_final:.2f1}")