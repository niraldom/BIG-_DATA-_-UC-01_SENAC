# estrutura de repetição infinita
i = 0
resp = "S"
while resp == "S"or resp == "s":
    print(i)
    i += 1
    resp = input("deseja continuar (S/N)? ")