# Exibir dados sobre roubo e furto de veículos 
import pandas as pd
def formatar(valor):
    return "{:.2f}%".format(valor)
roubo = pd.Series([100,90,80,120,110,90,70])
furto = pd.Series([80,60,70,60,100,50,30])
rec = pd.Series([70,50,60,80,100,70,50])
print("--- Soma Diária de Roubos e Furtos de Veículos ---")
print(roubo + furto)
print("\n--- Percentual Diário de Recuperação de Veículos ---")
tx_rec = ((rec / roubo) * 100).apply(formatar)
print(tx_rec)
print(f"\nTotal de Roubos de Veículos: {roubo.sum()}")
print(f"\nTotal de Furtos de Veículos: {furto.sum()}")
print(f"\nTotal de Recuperação de Veículos: {rec.sum()}")
tot_tx_rec = (rec.sum() / roubo.sum()) * 100
print(f"\nPercentual Total de Recuperação de Veículos: {tot_tx_rec:.2f}%")