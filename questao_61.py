def inverter(texto):
    return texto[::-1]

strings = [
    "python2023",
    "0203programacao2023",
    "luz azul",
    "arara rara",
    "anotaram a data da maratona"
]

for texto in strings:
    print(inverter(texto))
