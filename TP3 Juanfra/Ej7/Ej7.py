rta="s"
nums=[]
tot=0
rta=(input("Desea agregar un numero? S/N\n"))
while rta == "s" or rta == "S":
    num=int(input("Ingrese el numero que desea agregar: "))
    nums.append(num)
    rta=(input("Desea agregar un numero? S/N\n"))
for elemento in nums:
    tot+=elemento
    prom=tot/len(nums)
print(f"El promedio de los valores es: {prom}")