numeros = []
numeros.append(25)
numeros.append(150)
numeros.append(23)
numeros.append(44)
numeros.append(40)
numeros.append(130)
numeros.append(4)

mayor = 0
menor = 999

for x in numeros:
    if x > mayor:
        mayor = x
    
    if x < menor:
        menor = x

print(f"El numero mayor es: {mayor} y el numero menor es {menor}")