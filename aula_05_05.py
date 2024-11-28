# Programa para comparar listas
resp = ["A", "B", "C", "D","E"]
gab = ["A", "B", "B", "D","E"]
acertos = 0
erros = 0
for i in range(len(resp)):
    if resp[i] == gab[i]:
        acertos += 1
    else:
        erros += 1
print(f"A quantidade de acertos foi: {acertos}")
print(f"A quantidade de erros foi de: {erros}")
