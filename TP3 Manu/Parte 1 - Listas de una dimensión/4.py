lista = []
impares = 0
pares = 0

while True:
    n = input("Ingrese un número entero (presione S para terminar de ingresar números): ")
    if n.upper() == "S":
        break
    lista.append(int(n))
    
for n in lista:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Cantidad de números pares: {pares}\nCantidad de números impares: {impares}")
