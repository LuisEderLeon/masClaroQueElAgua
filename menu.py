import funcionesUsuarios as fUs
import funcionesServicios as fSe
import json

fileUs = open("usuarios.json","r")
fileSe = open("servicios.json","r")
usuarios = json.load(fileUs)
servicios = json.load(fileSe)
fileUs.close()
fileSe.close()

print("""⠀⠀⠀⠀⠀⠀⢀⣤⣶⡾⡿⠟⠿⠿⠿⠻⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀
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

fileUs = open("usuarios.json","w")
fileSe = open("servicios.json","w")
dumpSe = json.dumps(servicios,indent=4)
dumpUs = json.dumps(usuarios,indent=4)
fileSe.write(dumpSe)
fileSe.close()
fileUs.write(dumpUs)
fileUs.close()