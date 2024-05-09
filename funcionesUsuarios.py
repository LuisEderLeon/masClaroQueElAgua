def crearUsuario(usuarios):
    nombre = input("Ingrese el nombre del usuario nuevo: ")
    direccion = input("Ingrese la direccion del usuario: ")
    try:
        contacto = int(input("Ingrese el numero con el que se va a contactar al usuario: "))
    except ValueError:
        contacto = 0
        while contacto == 0:
            try:
                contacto = int(input("Error, solo se deben ingresar numeros, ingrese un numero valido: "))
            except ValueError:
                contacto = 0
    documento = input("Ingrese el documento del usuario: ")
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            print("Error, este usuario ya existe; no pueden haber dos usuarios con el mismo documento")
            return usuarios
    if input("¿Desea ingresar el status del usuario? Por defecto, se creara un usuario con status 'nuevo': ").lower() == "si":
        status = input("Ingrese el status del usuario (nuevo, regular, leal): ").lower()
        if (status != "regular" or status != "leal") and status != "nuevo":
            print("Status no valido, se le asignara 'nuevo' como status al usuario")
            status = "nuevo"
    else:
        status = "nuevo"
    servicios = []
    usuarios.append({"nombre":nombre,"direccion":direccion,"contacto":str(contacto),"documento":documento,"status":status,"servicios":servicios})
    return usuarios

def listarUsuarios(usuarios):
    lista = []
    for usuario in usuarios:
        lista.append(usuario.get("nombre"))
    print("Los usuarios actuales son: " + str(lista))
    if input("¿Desea conocer informacion extra de algun usuario en especifico? ").lower() == "si":
        documento = input("Ingrese el documento del usuario que desea conocer informacion a detalle: ")
        for usuario in usuarios:
            if usuario.get("documento") == documento:
                print(usuario)
                return None
        print("Error, documento no encontrado")

listaUsuarios = []
listaUsuarios = crearUsuario(listaUsuarios)
listarUsuarios(listaUsuarios)
