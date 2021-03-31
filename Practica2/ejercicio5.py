import string
frase = input("Ingrese una frase: ")
strng = input("Ingrese un string: ")
cant = 0
lista = frase.split()
for elem in lista:
    if strng.upper() == elem.strip(string.punctuation).upper():
        cant = cant + 1
print(cant)