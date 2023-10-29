divisas = {"DOLAR":"$", "EURO":"€", "YEN":"¥", "LIBRA":"£", "WON":"₩"}

def buscarDivisa():
    busqueda = input("Ingresa el nombre de la divisa que quieres buscar en mayusculas: ")

    if busqueda in divisas:
        print(f"Divisa {busqueda} equivale a {divisas[busqueda]}")
    else:
        print(f"No tenemos registro de esta divisa")
        buscarDivisa()

buscarDivisa()
