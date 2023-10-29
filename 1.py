productos = ["Papas", "Arroz", "Huevos", "Pan", "Tomates"]
precios = [1000, 500, 2700, 1600, 3200]

x = 0
diccionario = {}

while x < 5:
    diccionario.update({productos[x]:precios[x]})
    x += 1

print(diccionario)