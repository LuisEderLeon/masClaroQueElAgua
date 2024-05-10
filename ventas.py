from csv import DictReader,DictWriter
from funcionesUsuarios import requiereNumero
from reportes import reportes
from datetime import datetime

def consultarVentas(usuarios):
    documento = requiereNumero("Ingrese el documento del usuario que desea conocer las compras: ")
    listaCompras = []
    nombresLlaves = ["nombre","marca","referencia","cantidad","precio","fecha"]
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            try:
                with open("ventas/" + usuario.get("nombre") + str(documento) + ".csv") as ventas:
                    listaCompras = list(DictReader(ventas))
                    print("Compras realizadas por " + usuario.get("nombre") + ": ")
                    for compra in listaCompras:
                        print(compra)
            except FileNotFoundError:
                print("Este usuario no tiene compras")
            
            with open("ventas/" + usuario.get("nombre") + str(documento) + ".csv","w",newline="") as ventas:
                listaCompras = añadirVenta(listaCompras)
                escritor = DictWriter(ventas,fieldnames=nombresLlaves)
                escritor.writeheader()
                for compra in listaCompras:
                    escritor.writerow(compra)
                return None

    print("Error, documento no encontrado")
    reportes("Se intento ingresar un documento inexistente")

def añadirVenta(compras):
    if input("¿Desea añadir una venta al usuario? (si, no): ") == "si":
        with open("productos.csv") as fProductos:
            productos = list(DictReader(fProductos))
            print("Productos disponibles: ")
            for producto in productos:
                print(producto)
            nombre = input("Ingrese el nombre del producto que desea vender (nombre, marca): ")
            for producto in productos:
                if (producto.get("nombre") + ", " + producto.get("marca")) == nombre:
                    referencia = input("Ingrese la referencia del producto: ")
                    cantidad = requiereNumero("Ingrese la cantidad de productos comprados: ")
                    compras.append({"nombre":producto.get("nombre"),"marca":producto.get("marca"),"referencia":referencia,"cantidad":cantidad,"precio":producto.get("precio"),"fecha":datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
            print("Este producto no esta en el catalogo")
            reportes("Se intento ingresar un producto inexistente")
    return compras

def sugerirVenta(usuarios):
    documento = requiereNumero("Ingrese el documento del usuario que desea sugerir compras: ")
    listaCompras = []
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            try:
                with open("ventas/" + usuario.get("nombre") + str(documento) + ".csv") as ventas:
                    listaCompras = list(DictReader(ventas))
                    for compra in listaCompras:
                        print("")
            except FileNotFoundError:
                print("Este usuario no tiene compras")