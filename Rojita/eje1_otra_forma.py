#Pido una lista al usuario
lista=input("Ingresa una lista de numeros separados por comas: ")
lista=lista.split(",")

#Conviero cada caracter de la lista a entero
lista=[int(lista) for lista in lista]

#Los sumo con 'sum'
suma=sum(lista)
print(f"La suma de los numeros ingresados es: {suma}")