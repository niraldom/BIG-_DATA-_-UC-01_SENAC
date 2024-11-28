# Programa que armazena e lista os dados de um vetor
nomes = []
idades = []
for i in range(5):
    nomes.append(input("Informe o nome: "))
    idades.append(int(input("informe a idade: ")))
print("listagem dos usuários")
for i in range(len(nomes)):
    print(f"{nomes[i]} - {idades[i]}")