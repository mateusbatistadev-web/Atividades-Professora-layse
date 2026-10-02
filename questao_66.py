def calcular_animais(cabecas, pernas):
    coelhos = (pernas - 2 * cabecas) // 2
    galinhas = cabecas - coelhos

    return coelhos, galinhas

coelhos, galinhas = calcular_animais(35, 94)

print("Coelhos:", coelhos)
print("Galinhas:", galinhas)
