# Programa para analisar características da população

def main():
    habitantes = []

    print("Informe os dados de cada habitante. Digite 'sair' para finalizar.")

    while True:
        sexo = input("Sexo (masculino/feminino) ou 'sair': ").lower()
        if sexo == 'sair':
            break
        
        if sexo not in ['masculino', 'feminino']:
            print("Sexo inválido. Por favor, insira 'masculino' ou 'feminino'.")
            continue

        olhos = input("Cor dos olhos (verdes/castanhos): ").lower()
        if olhos not in ['verdes', 'castanhos']:
            print("Cor dos olhos inválida. Por favor, insira 'verdes' ou 'castanhos'.")
            continue

        cabelos = input("Cor dos cabelos (castanhos/pretos/louros): ").lower()
        if cabelos not in ['castanhos', 'pretos', 'louros']:
            print("Cor dos cabelos inválida. Por favor, insira 'castanhos', 'pretos' ou 'louros'.")
            continue

        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("Idade inválida. Por favor, insira um número inteiro.")
            continue

        habitantes.append({
            'sexo': sexo,
            'olhos': olhos,
            'cabelos': cabelos,
            'idade': idade
        })

    if habitantes:
        # a) A maior idade dos habitantes
        maior_idade = max(h['idade'] for h in habitantes)
        print(f"\nMaior idade dos habitantes: {maior_idade}")

        # b) Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive
        fem_18_35 = sum(1 for h in habitantes if h['sexo'] == 'feminino' and 18 <= h['idade'] <= 35)
        print(f"Quantidade de mulheres com idade entre 18 e 35 anos: {fem_18_35}")

        # c) Quantidade de indivíduos com olhos verdes e cabelos louros
        verdes_louros = sum(1 for h in habitantes if h['olhos'] == 'verdes' and h['cabelos'] == 'louros')
        print(f"Quantidade de indivíduos com olhos verdes e cabelos louros: {verdes_louros}")
    else:
        print("Nenhum dado de habitante foi inserido.")

if __name__ == "__main__":
    main()