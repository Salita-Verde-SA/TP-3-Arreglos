#Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
#suma de todos los elementos en la lista.
 
#Pido una lista al usuario
lista = input("Ingrese una lista de numeros separados por comas: " )
lista=lista.split(",")
print(lista)
suma=0
#Suma con el metodo 'for'
for i in range(0,len(lista)):
    suma+=int(lista[i])

#Los imprimo en pantalla
print(f"La suma de los numeros ingresados es: {suma}")
