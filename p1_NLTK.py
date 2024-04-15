import re

# El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
# - Se entiende por "palabra" CUALQUIER coosa entre espacios

carpeta_nombre="Documentos\\"
#archivo_nombre="documento2.txt"

with open(carpeta_nombre+"archivo_nuevo.txt","r") as archivo:
    texto=archivo.read()

expresion_regular=re.compile(r"...? ")

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))