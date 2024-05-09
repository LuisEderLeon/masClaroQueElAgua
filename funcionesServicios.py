def crearServicio(servicios):
    nombre = input("Ingrese el nombre del servicio nuevo: ").capitalize()
    descripcion = input("Ingrese la descripcion del servicio: ")
    precio = requiereNumero("Ingrese el precio del servicio: $")
    for servicio in servicios:
        if servicio.get("nombre") == nombre:
            print("Error, este servicio ya existe; no pueden haber dos servicios con el mismo nombre")
            return servicios
    servicios.append({"nombre":nombre,"descripcion":descripcion,"precio":precio})
    return servicios

def listarServicios(servicios):
    lista = []
    for servicio in servicios:
        lista.append(servicio.get("nombre"))
    print("Los servicios actuales son: " + str(lista))
    if input("¿Desea conocer informacion extra de algun servicio en especifico? (si, no): ").lower() == "si":
        nombre = input("Ingrese el nombre del servicio que desea conocer informacion a detalle: ")
        for servicio in servicios:
            if servicio.get("nombre") == nombre:
                print(servicio)
                return None
        print("Error, nombre no encontrado")

def eliminarServicios(servicios):
    nombre = input("Ingrese el nombre del servicio a eliminar: ")
    for servicio in servicios:
        if servicio.get("nombre") == nombre:
            servicios.remove(servicio)
            return servicios
    print("Error, nombre no encontrado")
    return servicios

def modificarServicios(servicios):
    nombre = input("Ingrese el nombre del servicio a modificar: ")
    for servicio in servicios:
        if servicio.get("nombre") == nombre:
            atributo = input("Ingrese el atributo que se desea cambiar del servicio (nombre, descripcion, precio): ").lower()
            try:
                if atributo == "precio":
                    precio = requiereNumero("Ingrese el nuevo precio del servicio: $")
                    servicios[servicios.index(servicio)][atributo] = precio
                else:
                    servicios[servicios.index(servicio)][atributo] = input("Ingrese el nuevo valor que desea ingresarle al atributo '" + atributo + "': ")
            except KeyError:
                print("Error, atributo no valido")
            return servicios
    print("Error, nombre no encontrado")
    return servicios

def requiereNumero(mensaje):
    try:
        atributo = int(input(mensaje))
    except ValueError:
        atributo = "0"
        while atributo == "0":
            try:
                atributo = int(input("Error, solo se deben ingresar numeros, ingrese un precio valido: $"))
            except ValueError:
                atributo = "0"
    return atributo