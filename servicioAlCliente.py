from funcionesUsuarios import requiereNumero
from datetime import datetime
from reportes import reportes

def añadirNuevaSituacion(usuarios):
    documento = requiereNumero("Ingrese el documento del usuario que desea añadirle una situacion de servicio al cliente: ")
    for usuario in usuarios:
        if usuario.get("documento") == documento:
            with open("servicioAlCliente/" + usuario.get("nombre") + str(documento) + ".txt","a",newline="") as cliente:
                fechaHora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                tipo = input("Ingrese la situacion que se presento (consulta, reclamacion, sugerencia): ").capitalize()
                if (tipo == "Consulta" or tipo == "Reclamacion" or tipo == "Sugerencia"):
                    mensaje = input("Describa lo que sucedio en la situacion: ").capitalize()
                    cliente.write(fechaHora + " - " + tipo + ": " + mensaje + "\n")
                    return None
                else:
                    print("Error, situacion de servicio al cliente no valida")
                    reportes("Se ingreso una situacion de servicio al cliente no valida")
    print("Error, documento no encontrado")
    reportes("Se intento ingresar un documento inexistente")
