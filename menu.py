import funcionesUsuarios as fUs
import funcionesServicios as fSe
from servicioAlCliente import añadirNuevaSituacion
from ventas import *
import json
from reportes import reportes
import os

fileUs = open("usuarios.json","r")
fileSe = open("servicios.json","r")
usuarios = json.load(fileUs)
servicios = json.load(fileSe)
fileUs.close()
fileSe.close()

opcion = "0"
while opcion != "6":
    os.system("clear")
    print("""
⠀⠀⠀⠀⠀⠀⢀⣤⣶⡾⡿⠟⠿⠿⠿⠻⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⢿⢏⡡⣄⣠⢠⣀⣄⣠⣀⣄⣉⠞⣿⢷⣤⡀⠀⠀⠀
⠀⠀⣠⣾⢿⣽⣻⢾⣽⣞⣷⣻⣞⡾⣵⣯⢾⣭⡿⣞⣯⣿⣳⣄⠀⠀
⠀⣴⡿⣽⣻⡾⣯⣿⢾⣽⡾⣷⣻⢿⣽⡾⣿⣽⣻⣽⣟⣾⣽⣻⣧⠀
⢰⡿⣽⣟⡷⣿⣽⢾⣻⣷⣻⣽⢯⣿⢾⣽⡷⣯⡇⢸⡾⡽⠊⣱⢿⡇
⣿⢿⡝⢊⣉⣉⠺⣿⠉⣷⠻⠽⠿⣽⠻⠾⢽⡷⠷⠺⣍⣠⡾⣯⣟⣿
⣿⣻⠀⣿⢯⣟⠶⢮⠀⡧⠔⢓⠀⣿⠀⣶⡎⢰⢶⡆⠸⣏⣉⣉⣸⢿
⣿⡽⣧⣈⣉⣉⣤⡿⣀⣇⣘⣛⣀⡿⣀⣷⣳⣈⣉⣁⣼⣻⢾⣽⢯⣿
⠸⣟⣷⣯⢿⣽⣾⣻⢿⡽⣯⢿⣽⣻⣟⡷⣿⣽⣻⣽⢾⣻⣯⣟⣯⡇
⠀⠻⣷⢯⣿⣞⡷⣟⣯⣿⣻⢯⡷⣟⡾⣟⣷⣯⣟⣾⢿⣽⣞⣯⡟⠀
⠀⠀⠙⢿⣳⣯⢿⣻⣽⡾⣽⢯⣻⣝⣻⡽⣾⣳⡿⣽⣻⣾⡽⠋⠀⠀
⠀⠀⠀⠀⠛⢽⣟⣯⡷⣟⣯⢿⣱⢯⣷⣻⣽⢷⣟⣿⡳⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠹⠿⣽⣻⣯⣿⢾⣽⠾⠟⠛⠈


Bienvenido al menu de administrativos de Claro

Ingrese una de las siguientes opciones
--------------------------------------------------------------------
CRUD de usuarios -> 1
CRUD de servicios -> 2
Añadir situacion de servicio al cliente -> 3
Consultar ventas de un cliente -> 4
Solicitar sugerencias de venta hacia un cliente -> 5
Salir -> 6
--------------------------------------------------------------------""")
    opcion = input("Opcion: ")
    print("--------------------------------------------------------------------")
    if opcion == "1":
    
        print("""Ingrese una de las siguientes opciones
--------------------------------------------------------------------
Crear usuario -> 1
Enlistar usuarios -> 2
Modificar usuario -> 3
Eliminar usuario -> 4
Registrar servicio a un usuario -> 5
Salir -> 6
--------------------------------------------------------------------""")
        opcion = input("Opcion: ")
        print("--------------------------------------------------------------------")
        if opcion == "1":
            usuarios = fUs.crearUsuario(usuarios)
            input("Oprima Enter para continuar ")
        elif opcion == "2":
            fUs.listarUsuarios(usuarios)
            input("Oprima Enter para continuar ")
        elif opcion == "3":
            usuarios = fUs.modificarUsuarios(usuarios)
            input("Oprima Enter para continuar ")
        elif opcion == "4":
            usuarios = fUs.eliminarUsuarios(usuarios)
            input("Oprima Enter para continuar ")
        elif opcion == "5":
            usuarios = fUs.añadirServicio(usuarios,servicios)
            input("Oprima Enter para continuar ")
        elif opcion == "6":
            opcion = "0"
        else: 
            reportes("El usuario intento ingresar una opcion no valida en el menu de Usuarios")
    elif opcion == "2":
    
        print("""Ingrese una de las siguientes opciones
--------------------------------------------------------------------
Crear servicio -> 1
Enlistar servicios -> 2
Modificar servicio -> 3
Eliminar servicio -> 4
Salir -> 5
--------------------------------------------------------------------""")
        opcion = input("Opcion: ")
        print("--------------------------------------------------------------------")
        if opcion == "1":
            servicios = fSe.crearServicio(servicios)
            input("Oprima Enter para continuar ")
        elif opcion == "2":
            fSe.listarServicios(servicios)
            input("Oprima Enter para continuar ")
        elif opcion == "3":
            usuarios = fSe.modificarServicios(servicios)
            input("Oprima Enter para continuar ")
        elif opcion == "4":
            usuarios = fSe.eliminarServicios(servicios)
            input("Oprima Enter para continuar ")
        elif opcion == "5":
            opcion == "0"
        else: 
            reportes("El usuario intento ingresar una opcion no valida en el menu de Usuarios")
            opcion == "0"
    elif opcion == "3":
        añadirNuevaSituacion(usuarios)
        input("Oprima Enter para continuar ")
    elif opcion == "4":
        consultarVentas(usuarios)
        input("Oprima Enter para continuar ")
    elif opcion == "5":
        sugerirVenta(usuarios)
        input("Oprima Enter para continuar ")
    elif opcion != "6":
        print("Ingrese una opcion valida")
        input("Oprima Enter para continuar ")
        reportes("El usuario intento ingresar una opcion no valida en el menu principal")

fileUs = open("usuarios.json","w")
fileSe = open("servicios.json","w")
dumpSe = json.dumps(servicios,indent=4)
dumpUs = json.dumps(usuarios,indent=4)
fileSe.write(dumpSe)
fileSe.close()
fileUs.write(dumpUs)
fileUs.close()