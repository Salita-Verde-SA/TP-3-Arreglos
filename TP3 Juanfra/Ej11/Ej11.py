salida = "s"
lista = []

while salida == "s":
    salida = input("Desea agregar un elemento? S/N")
    if salida == "s":
        elem = input("Ingrese el numero que desea agregar a la lista: ")
        lista.append(elem)

    contador = {}

    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1

print(f"La cantidad de veces que se repiten los elementos son:\n {contador}")
