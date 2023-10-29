informacion_usuario = {}

nombre = input("Ingresa tu nombre: ")
informacion_usuario.update({"Nombre": nombre})
apellido = input("Ingresa tu pellido: ")
informacion_usuario.update({"Apellido": apellido})
edad = input("Ingresa tu edad: ")
informacion_usuario.update({"Edad": edad})
apodo = input("Ingresa tu apodo: ")
informacion_usuario.update({"Apodo": apodo})
m_o_d = input("Marvel o DC: ")
informacion_usuario.update({"Fav": m_o_d})

print(informacion_usuario)
