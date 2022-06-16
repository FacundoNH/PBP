dolares = input("¿Cuantos dolares estadounidenses tenes?: ")
dolares = float(dolares)
valor_pesos = 0.0047
pesos = dolares / valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tenes $" + pesos + " pesos")