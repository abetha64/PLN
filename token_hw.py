import nltk
nltk.download('punkt')

carpeta_nombre="Documentos\\"
with open(carpeta_nombre+"archivo_nuevo.txt","r") as archivo:
    texto=archivo.read()
    tokens=nltk.word_tokenize(texto,"spanish")
    tokens_conjunto = set(tokens)
    totaldPalabras = len(tokens)
    palabrasDiferentes = len(tokens_conjunto)
    riqueza_lexica = palabrasDiferentes/totaldPalabras

print("PALABRAS TOTALES: ", riqueza_lexica)

#HOLA CARA PILIN#