#f = open("README_numpy", "r")
lista = []
#while(True):
#    linea = f.readline()
#    for elem in linea.split(" "):
#        lista.append(elem)
#    if not linea:
#        break
with open("README_numpy")as f:
    for lineas in f:
        lista.extend(lineas.split())
f.close()

dic={}
for elem in lista:
    if elem in dic:
        dic[elem]=dic[elem] + 1
    else:
        dic[elem]=1 

max=-1
for elem in dic:
    if dic[elem]>max:
        max = dic[elem]
        palabraMax = elem
print(palabraMax) 