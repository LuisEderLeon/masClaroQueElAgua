from reportes import reportes

def crearUsuario(usuarios):
    nombre = input("Ingrese el nombre del usuario nuevo: ")
    direccion = input("Ingrese la direccion del usuario: ")
    contacto = requiereNumero("Ingrese el numero con el que se va a contactar al usuario: ")
    documento = requiereNumero("Ingrese el documento del usuario: ")
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            print("Error, este usuario ya existe; no pueden haber dos usuarios con el mismo documento")
            reportes("Se intento crear un usuario con documento ya existente")
            return usuarios
    opcion = input("¿Desea ingresar el status del usuario? Por defecto, se creara un usuario con status 'nuevo' (si, no): ").lower() 
    if opcion == "si":
        status = input("Ingrese el status del usuario (nuevo, regular, leal): ").lower()
        if (status != "regular" and status != "leal") and status != "nuevo":
            print("Status no valido, se le asignara 'nuevo' como status al usuario")
            reportes("Se intento ingresar un status no valido")
            status = "nuevo"
    elif opcion != "no":
        print("Opcion no valida, se interpretara como 'no'")
        reportes("Se intento ingresar una opcion no valida")
        status = "nuevo"
    else:
        status = "nuevo"
    servicios = []
    usuarios.append({"nombre":nombre,"direccion":direccion,"contacto":contacto,"documento":documento,"status":status,"servicios":servicios})
    return usuarios

def listarUsuarios(usuarios):
    lista = []
    for usuario in usuarios:
        lista.append(usuario.get("nombre") + ": " + str(usuario.get("documento")))
    print("Los usuarios actuales son: " + str(lista))
    opcion = input("¿Desea conocer informacion extra de algun usuario en especifico? (si, no): ").lower()
    if opcion == "si":
        documento = requiereNumero("Ingrese el documento del usuario que desea conocer informacion a detalle: ")
        for usuario in usuarios:
            if usuario.get("documento") == documento:
                print("Nombre: " + usuario["nombre"])
                print("Direccion: " + usuario["direccion"])
                print("Numero de contacto: " + str(usuario["contacto"]))
                print("Documento: " + str(usuario["documento"]))
                print("Status: " + usuario["status"])
                print("Servicios: " + str(usuario["servicios"]))
                return None
        print("Error, documento no encontrado")
        reportes("Se intento ingresar un documento inexistente")
    elif opcion != "no":
        print("Opcion no valida, se interpretara como 'no'")
        reportes("Se intento ingresar una opcion no valida")

def eliminarUsuarios(usuarios):
    documento = requiereNumero("Ingrese el documento del usuario a eliminar: ")
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            usuarios.remove(usuario)
            return usuarios
    print("Error, documento no encontrado")
    reportes("Se intento ingresar un documento inexistente")
    return usuarios

def modificarUsuarios(usuarios):
    documento = requiereNumero("Ingrese el documento del usuario a modificar: ")
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            atributo = input("Ingrese el atributo que se desea cambiar del usuario (nombre, direccion, contacto, status): ").lower()
            try:
                if atributo == "contacto":
                    contacto = requiereNumero("Ingrese el numero con el que se va a contactar al usuario: ")
                    usuarios[usuarios.index(usuario)][atributo] = contacto
                elif atributo == "status":
                    status = input("Ingrese el status del usuario (nuevo, regular, leal): ").lower()
                    if (status != "regular" and status != "leal") and status != "nuevo":
                        print("Status no valido, se le asignara 'nuevo' como status al usuario")
                        reportes("Se intento ingresar un status no valido")
                        status = "nuevo"
                    usuarios[usuarios.index(usuario)][atributo] = status
                elif atributo == "documento":
                    print("Error, el documento de un usuario no es modificable, puesto que este es unico para cada usuario")
                    reportes("Se intento modificar el documento de un usuario")
                else:
                    usuarios[usuarios.index(usuario)][atributo] = input("Ingrese el nuevo valor que desea ingresarle al atributo '" + atributo + "': ")
            except KeyError:
                print("Error, atributo no valido")
                reportes("Se intento ingresar una llave inexistente")
            return usuarios
    print("Error, documento no encontrado")
    return usuarios

def añadirServicio(usuarios,servicios):
    nServicio = input("Ingrese el nombre del servicio a registrarle al usuario: ").capitalize()
    for servicio in servicios:
        if servicio.get("nombre") == nServicio:
            documento = requiereNumero("Ingrese el documento del usuario al cual se le registrara el servicio '"+nServicio+"': ")
            for usuario in usuarios:
                if usuario.get("documento") == documento:
                    usuarios[usuarios.index(usuario)]["servicios"].append(nServicio)
                    return usuarios
            print("Error, documento no encontrado")
            reportes("Se intento ingresar un documento inexistente")
            return usuarios
    print("Error, servicio no encontrado")
    reportes("Se intento ingresar un servicio inexistente")
    return usuarios

def requiereNumero(mensaje):
    try:
        atributo = int(input(mensaje))
    except ValueError:
        atributo = "0"
        while atributo == "0":
            try:
                reportes("Se intento ingresar un caracter a una variable de tipo numero")
                atributo = int(input("Error, solo se deben ingresar numeros, ingrese un numero valido: "))
            except ValueError:
                atributo = "0"
    return atributo