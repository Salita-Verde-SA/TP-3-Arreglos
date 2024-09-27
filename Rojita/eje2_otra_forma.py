lista=input("Ingresa una lista de numeros positivos separados por una coma: ")
lista=lista.split(",")
min=1000000
max=0

#Convierto los caracteres a enteros en una nueva lista "lista_numeros"
lista_numeros=[int(numero) for numero in lista]
print(lista_numeros)
for i in range(0,len(lista)):
    if lista_numeros[i] > max:
        max=lista_numeros[i]
    if lista_numeros[i] < min:
        min=lista_numeros[i]
print(f"Numero mayor: {max}")
print(f"Numero menor: {min}")