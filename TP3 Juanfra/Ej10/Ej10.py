def eliminarxInd(lista):
    opc = int(input("Ingrese la posicion del valor que desea eliminar: "))
    del lista[opc - 1]
    print(f"La lista con el valor eliminado es: {lista}")


rta = "s"
lista = []

while rta == "s":
    rta = input("Desea agregar un elemento? S/N")
    if rta == "s":
        elem = input("Ingrese el numero que desea agregar a la lista: ")
        lista.append(elem)
eliminarxInd(lista)
s