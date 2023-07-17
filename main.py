import os 
import citas

if __name__ == '__main__':
    isActive = True
    op = 0
    while isActive:
        try:
            os.system("clear")
            print("------------------------------")
            print("-------- Menu de Citas -------")
            print("------------------------------")
            print("1. Gestionar Cita")
            print("2. Salir del programa")

            op = int(input("Ingrese una opción: "))
            if op == 1:
                citas.loadInfoCitas()
                citas.mainMenu()
            elif op == 2:
                isActive = False
            else:
                print("opcion invalida")
                input("")
        except ValueError:
            print("ERROR!!!")
            input("")