def contar_caractere(texto, caractere):
    quantidade = texto.count(caractere)
    return quantidade

texto = input("Digite uma string: ")
caractere = input("Digite o caractere: ")

resultado = contar_caractere(texto, caractere)

print("O caractere aparece", resultado, "vez(es).")
