lista=input("Ingresa una lista de numeros separados por comas: ")
lista=lista.split(",")
#Convierto los elementos de la lista a enteros
lista=[int(lista) for lista in lista ]
num=int(input("Ingrese un numero para multiplicar cada numero de la lista anterior: "))
lista=[lista*num for lista in lista]
print(lista)