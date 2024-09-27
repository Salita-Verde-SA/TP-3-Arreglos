lista=input("Ingresa una lista de numeros separados por comas: ")
lista=lista.split(",")
#Convierto los elementos de la lista a enteros
lista=[int(lista) for lista in lista ]
suma=sum(lista)
print(len(lista))
print(f"El promedio de la lista es: {suma/len(lista)}")