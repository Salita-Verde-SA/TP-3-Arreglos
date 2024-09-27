
    
    

lista=input("Ingresa una lista de numeros separados por comas: ")
lista=lista.split(",")
#Convierto los elementos de la lista a enteros
lista=[int(elemento) for elemento in lista ]

contador={}

for elemento in lista:
    if elemento % elemento==0:
        contador[elemento]+=1
    else: 
        contador[elemento]=1
print(contador)

