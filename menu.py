import funcionesUsuarios as fUs
import funcionesServicios as fSe
import json

fileUs = open("usuarios.json","r")
fileSe = open("servicios.json","r")
usuarios = json.load(fileUs)
servicios = json.load(fileSe)
fileUs.close()
fileSe.close()

servicios = fSe.crearServicio(servicios)
usuarios = fUs.crearUsuario(usuarios)
usuarios = fUs.añadirServicio(usuarios,servicios)
fUs.listarUsuarios(usuarios)

fileUs = open("usuarios.json","w")
fileSe = open("servicios.json","w")
dumpSe = json.dumps(servicios,indent=4)
dumpUs = json.dumps(usuarios,indent=4)
fileSe.write(dumpSe)
fileSe.close()
fileUs.write(dumpUs)
fileUs.close()