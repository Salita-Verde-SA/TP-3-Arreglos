def encontrar_repetidos(lista):
    contador = {}

    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1

    repetidos = [elemento for elemento, cantidad in contador.items() if cantidad > 1]

    return repetidos


rta = "s"
lista = []

while rta == "s":
    rta = input("Desea agregar un elemento? S/N")
    if rta == "s":
        elem = input("Ingrese lo que desee agregar a la lista: ")
        lista.append(elem)

elementos_repetidos = encontrar_repetidos(lista)
print(f"Los elementos repetidos son: {elementos_repetidos}")
