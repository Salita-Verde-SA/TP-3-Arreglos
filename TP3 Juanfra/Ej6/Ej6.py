salida = "s"
nums = []
salida = input("Desea agregar un numero? S/N\n")
while salida == "s" or salida == "S":
    num = int(input("Ingrese el numero que desea agregar: "))
    nums.append(num)
    salida = input("Desea agregar un numero? S/N\n")
s = set(nums)
print(f"El arreglo sin duplicados es: {s}")
