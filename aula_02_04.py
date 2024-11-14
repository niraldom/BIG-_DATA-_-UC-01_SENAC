# Programa sua Idade
import datetime # importa a biblioteca datetime
data_atual = datetime.date.today() # armazena na variável a data completa
ano_atual = data_atual.year # armazena na variável o ano atual
ano_nascimento = int(input("informe o ano de nascimento"))
idade = (ano_atual - ano_nascimento)
print(f"sua idade é de {idade}")