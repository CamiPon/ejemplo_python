import string
letra = input("Ingrese una letra: ")
lista = []
if letra in string.ascii_letters:
    with open("README_numpy")as f:
        for lineas in f:
            lista.extend(lineas.split())
    f.close()
    for palabras in lista:
        if letra.upper == palabras[0].upper():
            print(palabras.strip(string.punctuation))
else:
    print("No se ha ingresado una letra")
#Imprime las palabras repetidas, para que no suceda esto basta con crear un diccionario