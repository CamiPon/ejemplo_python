import string
frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple."""
lista = frase.split()
dic = {}
lista1 = []
#for palabra in lista:
#    aux = palabra.strip(string.punctuation).lower()
#    dic[aux] = 0
#for elem in dic:
#    lista1.append(elem)
for palabra in lista:
    aux = palabra.strip(string.punctuation).lower()
    if aux not in lista1:
        lista1.append(aux)
print(lista1)