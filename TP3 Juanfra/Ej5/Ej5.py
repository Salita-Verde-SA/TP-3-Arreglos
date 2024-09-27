rta = "s"
nums = []
tot = 1
rta = input("Desea agregar un numero? S/N\n")
while rta == "s" or rta == "S":
    num = int(input("Ingrese el numero que desea agregar: "))
    nums.append(num)
    rta = input("Desea agregar un numero? S/N\n")
for elemento in nums:
    tot *= elemento
print(f"El producto entre todos los elementos es: {tot}")
