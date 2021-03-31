f = open("README_numpy", "r")
while(True):
    linea = f.readline()
    if "http" in linea:
        print(linea)
    if not linea:
        break
f.close()