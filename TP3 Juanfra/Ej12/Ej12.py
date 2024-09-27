import numpy as np
rta="s"
lista1=[]

while rta=="s":
    rta=input("Desea agregar un elemento? S/N")
    if rta=="s":
        elem=input("Ingrese el numero que desea agregar a la lista 1: ")
        lista1.append(elem)

cont=0
rta="s"
lista2=[]

while cont<len(lista1):
        elem=input("Ingrese el numero que desea agregar a la lista 2: ")
        lista2.append(elem)
        cont+=1
listaSuma=[]
for i in range (0,len(lista1)):
     listaSuma.append(int(lista1[i])+int(lista2[i]))
print(f"La suma de las listas elemento a elemento es: \n {listaSuma}")