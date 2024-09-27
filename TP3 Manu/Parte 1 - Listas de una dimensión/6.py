lista = []

while True:
    n = input("Ingrese un número (presione S para terminar de ingresar números): ")
    if n.upper() == "S":
        break
    lista.append(n)

lista = list(set(lista))

print(f"Lista final: {lista}")