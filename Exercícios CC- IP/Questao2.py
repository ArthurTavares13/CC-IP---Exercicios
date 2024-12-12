def gerar_tabuada():

    print("Bem-vindo ao gerador de tabuada!")
    try:
        numero = int(input("Digite um número: "))
        print(f"Tabuada do {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

gerar_tabuada()
