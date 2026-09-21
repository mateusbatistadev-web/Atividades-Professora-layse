def fahrenheit_para_celsius(f):
    c = (5 / 9) * (f - 32)
    return c

temperatura = float(input("Digite a temperatura em Fahrenheit: "))

print("Temperatura em Celsius:", fahrenheit_para_celsius(temperatura))
