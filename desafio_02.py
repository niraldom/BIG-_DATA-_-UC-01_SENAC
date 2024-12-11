# Programa para ler e calcular temperaturas 

def main():
    temperaturas = []

    print("Digite as temperaturas (uma por vez). Digite 'sair' para finalizar.")

    while True:
        entrada = input("Informe a temperatura ou 'sair': ")
        
        if entrada.lower() == 'sair':
            break

        try:
            temperatura = float(entrada)
            temperaturas.append(temperatura)
        except ValueError:
            print("Por favor, insira um valor numérico válido ou 'sair'.")

    if temperaturas:
        menor = min(temperaturas)
        maior = max(temperaturas)
        media = sum(temperaturas) / len(temperaturas)

        print(f"\nMenor temperatura: {menor:.2f}°C")
        print(f"Maior temperatura: {maior:.2f}°C")
        print(f"Média das temperaturas: {media:.2f}°C")
    else:
        print("Nenhuma temperatura foi inserida.")

if __name__ == "__main__":
    main()
