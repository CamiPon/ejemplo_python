import string
nombres = []
eval1 = []
eval2 = []

with open("nombres")as f:
    for lineas in f:
        nombres.extend(lineas.split())
f.close()
with open("eval1")as f:
    for lineas in f:
        eval1.extend(lineas.split())
f.close()
with open("eval2")as f:
    for lineas in f:
        eval2.extend(lineas.split())
f.close()

#la que viene es una mala forma  de resolver

#lista = []
#suma = 0
#for elem in range(len(nombres)):
#    aux = int(eval1[elem].strip(",")) + int(eval2[elem].strip(","))
#    lista.append(((nombres[elem].strip(string.punctuation)),aux))
#    suma = suma + aux
#prom = suma / len(nombres)
#print(prom)
#print(f"Los que obtuvieron promedio menos que", prom, "son")
#for elem in lista:
#    if elem[1] < prom:
#        print(elem[0])
total = []
for nota1, nota2 in zip(eval1,eval2):
    total.append(sum([int(nota1.strip(string.punctuation)),int(nota2.strip(string.punctuation))]))
notas = list(zip(nombres,total))
suma = 0
for tot in total:
    suma = suma + tot
prom = suma / len(total)
print(f"Los que obtuvieron promedio menos que", prom, "son: ")
for elem in notas:
    if elem[1] < prom:
        print(elem[0])