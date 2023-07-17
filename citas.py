import core 
import os 

""" 
from datetime import datetime
from datetime import timedelta 
""" 

diccCitas = {"data":[]}

def loadInfoCitas():
    global diccCitas
    if(core.chekFile("citas.json")):
        diccCitas = core.loadInfo("citas.json")
    else:
        core.crearInfo("citas.json", diccCitas)

def mainMenu():
    try:
        os.system("clear")
        isCitasRun = True
        op = 0

        print("----------------------------------------------------------------")
        print("--------------- Bienvenido a gestion de citas ------------------")
        print("----------------------------------------------------------------")
        print("1. agregar cita")
        print("2. Buscar citas")
        print("3. Modificar cita")
        print("4. Eliminar cita")
        print("5. Volver al inicio")
        op = int(input("Ingrese una opcion: "))

        if op == 1:
            os.system("clear")
            print("----------------------------------------------------------------")
            print("---------------------- Agregar Cita ----------------------------")
            print("----------------------------------------------------------------")
            idAut = 0
            if(len(diccCitas["data"]) >= 1):
                idAut = diccCitas["data"][-1]["id"] + 1
            else:
                idAut = 1
            nombre = input("Ingrese el nombre: ").lower()
            fecha = input("Ingrese la fecha [aaaa-mm-dd HH:mm]: ")
            print("[1]am -- [2]pm")
            validarHora = int(input(": "))
            if validarHora == 1:
                hora = "am"
            elif validarHora == 2:
                hora = "pm"
            else:
                print("Se le asigno por la mañana ")
                hora = "am"
            data = {
                "id": idAut,
                "nombre": nombre,
                "fecha": fecha,
                "hora": hora,
                "motivo": input("Ingre su motivo de cita: ").lower()
            }
            
            diccCitas["data"].append(data)
            core.crearInfo("citas.json",data)
            
        elif op == 2:
            try:
                os.system("clear")
                print("----------------------------------------------------------------")
                print("------------------------ Buscar Cita ---------------------------")
                print("----------------------------------------------------------------")
                print("1. Buscar por Nombre ")
                print("2. Buscar por Fecha ")
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    nomSearch = input("Ingrese el nombre del citador: ").lower()
                    for i,item in enumerate(diccCitas["data"]):
                        if nomSearch == item["nombre"]:
                            print("------------------------------------")
                            print(f"Id: {item['id']}")
                            print(f"Nombre: {item['nombre']}")
                            print(f"Fecha: {item['fecha']}")
                            print(f"Hora: {item['hora']}")
                            print(f"Motivo: {item['motivo']}")
                            print("------------------------------------")
                            input("")
                elif opcion == 2:
                    fechSerach = input("Ingrese la fecha: ")
                    for i,item in enumerate(diccCitas["data"]):
                        if fechSerach == item["fecha"]:
                            print("------------------------------------")
                            print(f"Id: {item['id']}")
                            print(f"Nombre: {item['nombre']}")
                            print(f"Fecha: {item['fecha']}")
                            print(f"Hora: {item['hora']}")
                            print(f"Motivo: {item['motivo']}")
                            print("------------------------------------")
                            input("")
                else:
                    print("Opcion invalida")
                    input("")
            except ValueError:
                print("ERROR!!!")
                input("")
        elif op == 3:
            try:
                os.system("clear")
                print("----------------------------------------------------------------")
                print("-------------------- Modificar Datos Cita ----------------------")
                print("----------------------------------------------------------------")
                print("1. Modificar con el id: ")
                print("2. Modificar con el nombre: ")

                opcion = int(input("Ingrese una opcion: "))

                if opcion == 1:
                    idSearch = int(input("Ingrese el id a modificar: "))
                    for i,item in enumerate(diccCitas["data"]):
                        if idSearch == item["id"]:
                            item["nombre"] = input(f'Nombre: {item["nombre"]} -- Ingrese el nuevo nombre o presione ENTER para omitir: ').lower() or item["nombre"]
                            item["fecha"] = input(f'Fecha: {item["fecha"]} -- Ingrese la nueva fecha o presione ENTER para omitir: ') or item["fecha"]
                            item["hora"] = input(f'Hora: {item["hora"]} -- Ingrese al horario de asistencia [AM -- PM]: ').lower() or item["hora"]
                            item["motivo"] = input(f'Motivo: {item["motivo"]} -- Ingrese el nuevo motivo o presione ENTER para omitir: ').lower() or item["motivo"]
                            core.editarData("citas.json",diccCitas)
                elif opcion == 2:
                    nomSearch = input("Ingrese el nombre a modificar: ").lower()
                    for i,item in enumerate(diccCitas["data"]):
                        if nomSearch == item["nombre"]:
                                print(f'id: {item["id"]}')
                                item["nombre"] = input(f'Nombre: {item["nombre"]} -- Ingrese el nuevo nombre o presione ENTER para omitir: ').lower() or item["nombre"]
                                item["fecha"] = input(f'Fecha: {item["fecha"]} -- Ingrese la nueva fecha o presione ENTER para omitir: ') or item["fecha"]
                                item["hora"] = input(f'Hora: {item["hora"]} -- Ingrese al horario de asistencia [AM -- PM]: ').lower() or item["hora"]
                                item["motivo"] = input(f'Motivo: {item["motivo"]} -- Ingrese el nuevo motivo o presione ENTER para omitir: ').lower() or item["motivo"]
                                core.editarData("citas.json",diccCitas)
                else:
                    print("Opcion invalida")
                    input("")

            except ValueError:
                print("ERROR!!!")
                input("")
        elif op == 4:
            try:
                os.system("clear")
                print("----------------------------------------------------------------")
                print("----------------------- Eliminar Cita --------------------------")
                print("----------------------------------------------------------------")
                print("1. Eliminar por Id")
                print("2. Eliminar por Fecha")
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    idSearch = int(input("Ingrese el id a eliminar: "))
                    for i,item in enumerate(diccCitas["data"]):
                        if idSearch == item["id"]:
                            diccCitas["data"].pop(i)
                            core.editarData("citas.json",diccCitas)
                elif opcion == 2:
                    fechSerach = input("Ingrese la fecha a eliminar: ")
                    for i,item in enumerate(diccCitas["data"]):
                        if fechSerach == item["fecha"]:
                            diccCitas["data"].pop(i)
                            core.editarData("citas.json",diccCitas)
                else:
                    print("Opcion invalida")
                    input("")
            except ValueError:
                print("ERROR!!!")
                input("")
        elif op == 5:
            isCitasRun = False
        if isCitasRun:
            mainMenu()
        else:
            input("")
    except ValueError:
        print("ERROR!!!")
        input("")
