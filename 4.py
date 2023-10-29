numeros = [5,8,10,22,28,32,38,45,49,50]

x = 10
cadena = ""
while x != 0:
    x -= 1
    cadena += str(numeros[x])
    if x != 0:
        cadena += ","

print(cadena)