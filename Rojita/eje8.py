lista=input("Ingresa una lista de numeros separados por comas: ")
lista=lista.split(",")
#Convierto los elementos de la lista a enteros
lista=[int(lista) for lista in lista ]

contador= {}

for elemento in lista:
    if elemento in contador:
        contador[elemento]+=1
    else: 
        contador[elemento]=1
        
repetidos=[clave for clave , valor in contador.items() if valor > 1]
print(f"Los repetidos son: {repetidos}")