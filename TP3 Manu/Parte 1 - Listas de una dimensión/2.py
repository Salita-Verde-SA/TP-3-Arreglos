lista = []

while True:
    n = input("Ingrese un número (presione S para terminar de ingresar números): ")
    if n.upper() == "S":
        break
    lista.append(float(n))

mayor: float = 0

if len(lista) > 1:
    for e in lista:
        for n in lista:
            if n > e and n > mayor:
                mayor = n  
else:
    mayor = lista[0]
    
print(mayor)