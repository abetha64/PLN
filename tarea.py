

carpeta_nombre="Documentos\\" 
 
with open(carpeta_nombre+ "archivo_nuevo.txt","r") as archivo: #lee un archivo
    texto=archivo.read() 
palabras_lista=texto.split() #separa las palabras
palabras_lista.sort() 
for palabra in palabras_lista: 
    print(palabra)  
