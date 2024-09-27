rta = "s"
nums = []
contp = 0
conti = 0
rta = input("Desea agregar un numero? S/N\n")
while rta == "s" or rta == "S":
    num = int(input("Ingrese el numero que desea agregar: "))
    nums.append(num)
    rta = input("Desea agregar un numero? S/N\n")
for elemento in nums:
    if elemento % 2 == 0:
        contp += 1
    else:
        conti += 1
print(
    f"La cantidad de elementos pares es: {contp}\nLa cantidad de elementos impares es: {conti}"
)
