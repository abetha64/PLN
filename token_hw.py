import nltk
nltk.download('punkt')

carpeta_nombre="Documentos\\"
with open(carpeta_nombre+"archivo_nuevo.txt","r") as archivo:
    texto=archivo.read()
    tokens=nltk.word_tokenize(texto,"spanish")
    for token in tokens:
        print(token)
    
palabras_total=len(tokens)
print("PALABRAS TOTALES: ", palabras_total)
