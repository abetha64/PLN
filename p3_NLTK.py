# Alba BethbiraiLópezAguilar
import nltk

print("Hola! Soy Alba CEO CENTER")

carpeta_nombre = "Documentos\\"


with open(carpeta_nombre + "archivo_nuevo.txt", "r") as archivo:
    texto = archivo.read()

print("----------------------------------------------------------------------")

palabras_funcionales = nltk.corpus.stopwords.words("spanish")

for palabras_funcional in palabras_funcionales:
    '''print(palabras_funcional)'''
    
print("----------------------------------------------------------------------")

tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = []

for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)
        '''print(tokens_limpios)'''

print("TOTALIDAD DE TOKENS: ",len(tokens))
print("TOTALIDAD DE TOKENS LIMPIOS: ",len(tokens_limpios))

texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)
