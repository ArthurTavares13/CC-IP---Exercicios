def calcular_media():
    
    print("Insira as notas.")

    notas = []

    while True:
        try:
            entrada = input("Digite a nota: ")
            nota = float(entrada)

            if nota == -1:
                break

            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Por favor, insira um número entre 0 e 10.")
        except ValueError:
            print("Erro: Valor informado não é válido. Insira apenas números.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"A média das notas inseridas é: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

calcular_media()
