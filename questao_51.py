temperaturas = []

for i in range(5):
    temperatura = float(input(f"Digite a temperatura do dia {i + 1}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)

print("\nTemperaturas:", temperaturas)
print("Média:", media)

if 18 <= media <= 28:
    print("A média está dentro da faixa ideal.")
else:
    print("A média está fora da faixa ideal.")
