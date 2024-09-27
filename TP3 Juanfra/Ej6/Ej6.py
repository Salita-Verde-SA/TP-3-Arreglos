rta="s"
nums=[]
rta=(input("Desea agregar un numero? S/N\n"))
while rta == "s" or rta == "S":
    num=int(input("Ingrese el numero que desea agregar: "))
    nums.append(num)
    rta=(input("Desea agregar un numero? S/N\n"))
s=set(nums)
print(f"El arreglo sin duplicados es: {s}")