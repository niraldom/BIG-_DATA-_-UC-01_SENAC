#
nomes_01 = "Alessandro, Maria, Eduarada"
nomes_02 = ["Alessandro", "Maria", "Eduarada"]
print(nomes_01)
print(nomes_02)
print(nomes_02[0])
print(len(nomes_02))
print("listagem dos elementos do vetor")
n = 1
for i in range(len(nomes_02)):
    print(f"{n}  - {nomes_02[i]}")
    n += 1