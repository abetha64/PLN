import nltk

carpeta_nombre="Documentos\\"
#archivo_nombre="P_IFT_290216_73_Acc.txt"

with open(carpeta_nombre+"archivo_nuevo.txt","r") as archivo:
    texto=archivo.read()
    tokens=nltk.word_tokenize(texto,"spanish")
    texto_nltk=nltk.Text(tokens)
    
    palabra_buscada = "Aplicaciones"
    print(f"Concordancia de '{palabra_buscada}':")
    texto_nltk.concordance(palabra_buscada)

    # Encontrar palabras similares a una palabra dada
    palabra_similar = "es"
    print(f"Palabras similares a '{palabra_similar}':")
    texto_nltk.similar(palabra_similar)



