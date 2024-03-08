import nltk

def riqueza_lexica(tokens):
    tokens_conjunto=set(tokens)
    palabras_totales=len(tokens)
    palabras_diferentes=len(tokens_conjunto)
    riqueza_lexica=palabras_diferentes/palabras_totales
    return riqueza_lexica

carpeta_nombre="Documentos\\"

with open(carpeta_nombre+"archivo_nuevo.txt","r") as archivo:
 texto=archivo.read()
 tokens=nltk.word_tokenize(texto,"spanish")
 riqueza_lexica=riqueza_lexica(tokens)
 print(riqueza_lexica)