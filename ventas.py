from csv import DictReader,DictWriter
from funcionesUsuarios import requiereNumero
from reportes import reportes
from datetime import datetime
import os

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
            if listaCompras == []:
                os.remove("ventas/" + usuario.get("nombre") + str(documento) + ".csv")
            return None

    print("Error, documento no encontrado")
    reportes("Se intento ingresar un documento inexistente")

def añadirVenta(compras):
    opcion = input("¿Desea añadir una venta al usuario? (si, no): ")
    if opcion == "si":
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
                    return compras
            print("Este producto no esta en el catalogo")
            reportes("Se intento ingresar un producto inexistente")
    elif opcion != "no":
        print("Opcion no valida, se interpretara como 'no'")
        reportes("Se intento ingresar una opcion no valida")
    return compras

def sugerirVenta(usuarios):
    documento = requiereNumero("Ingrese el documento del usuario que desea sugerir compras: ")
    listaCompras = []
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            try:
                with open("ventas/" + usuario.get("nombre") + str(documento) + ".csv") as ventas:
                    listaCompras = list(DictReader(ventas))
                    mayorCantidad = 0
                    for compra in listaCompras:
                        if int(compra.get("cantidad")) >= mayorCantidad:
                            mayorCantidad = int(compra.get("cantidad"))
                            mayorProducto = compra.get("nombre") + ", " + compra.get("marca")
                    print("Basado en las compras pasadas, se puede sugerir al usuario el siguiente producto: " + mayorProducto)
            except FileNotFoundError:
                print("Este usuario no tiene compras")