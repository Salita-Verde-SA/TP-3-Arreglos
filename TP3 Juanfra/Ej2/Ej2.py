rta="s"
nums=[]
rta=(input("Desea agregar un numero? S/N\n"))
while rta == "s" or rta == "S":
    num=int(input("Ingrese el numero que desea agregar: "))
    nums.append(num)
    rta=(input("Desea agregar un numero? S/N\n"))
maximo=max(nums)
minimo=min(nums)
print(f"El numero maximo del arreglo es {maximo} y el minimo es {minimo}")