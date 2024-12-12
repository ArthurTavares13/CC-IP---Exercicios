def contar_vogais_e_consoantes():
    print("Contador de vogais e consoantes")

    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"

    frase = input("Digite uma frase: ").lower()

    contador_vogais = 0
    contador_consoantes = 0

    for caractere in frase:
        if caractere in vogais:
            contador_vogais += 1
        elif caractere in consoantes:
            contador_consoantes += 1

    print(f"A frase contém {contador_vogais} vogais e {contador_consoantes} consoantes.")

contar_vogais_e_consoantes()
