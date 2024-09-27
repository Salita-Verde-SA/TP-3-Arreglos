rta = "s"
nums = []
rta = input("Desea agregar un numero? S/N\n")
while rta == "s" or rta == "S":
    num = int(input("Ingrese el numero que desea agregar: "))
    nums.append(num)
    rta = input("Desea agregar un numero? S/N\n")
nums.reverse()
res = nums
print(f"El arreglo invertido es: {res}")
