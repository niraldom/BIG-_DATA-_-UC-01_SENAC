# Programa para tratar erro de entrada de dados
nome = input("informe o nome: ")
while True:
    sexo = input("informe o sexo(M ou F) ")
    if sexo == "M" or sexo == "F":
        break
    else:
        print(f"informe apenas M ou F para o sexo")
while True:
    try:
        idade = int(input("informe sua idade "))
    except ValueError:
        print("verifique a idade digitada")
    else:
        print(f"Seja bem vindo {nome}")
        break