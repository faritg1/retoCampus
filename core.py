import json 

def crearInfo(*args):
    if (chekFile(args[0]) == False):
        with open('data/'+args[0],'w') as writeFile:
            json.dump(args[1],writeFile, indent=4)
            writeFile.close()
    else:
        with open('data/'+args[0],'r+') as f:
            file = json.load(f)
            file["data"].append(args[1])
            f.seek(0)

            json.dump(file,f,indent=4)
            f.close()

def editarData(*args):
    with open('data/'+args[0],'w') as writeFile:
        json.dump(args[1],writeFile, indent=4)
        writeFile.close()

def loadInfo(filaName):
    if (chekFile(filaName) == True):
        with open('data/'+filaName,'r') as readFile:
            dicc = json.load(readFile)
        return dicc

def chekFile(filaName):
    try:
        with open('data/'+filaName,'r') as r:
            return True
    except FileNotFoundError as e:
        print("Error!")
        return False
    except IOError as e:
        return False