def conversor(tipo_pesos, valor_dolar):
    pesos = input ("¿Cuantos pesos " + tipo_pesos + " tenes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tenes $" + dolares + " dólares")
menu = """
Bienvenido al conversor de monedas 💱

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3900)
elif opcion == 2: 
    conversor("argentinos", 214)
elif opcion == 3:
    conversor("mexicanos", 20.20)
else:
    print("Ingresa una opción correcta por favor")