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
 tokens=nltk.word_tokenize(texto,"spanish")#indica el lenguaje
 riqueza_lexica=riqueza_lexica(tokens)
 #print(riqueza_lexica)

#odatu comoestas //comentario sin lugar alguna
conteo_individual=tokens.count("los") #palabra a buscar
print("TOTAL DE VECES EN TEXTO => ",conteo_individual) #imprime el numero de veces que aparece en el texto
palabras_totales=len(tokens)#palabrasTotales son aquellas que existen en general en el txto, y te arroja cuantas existens
porcentaje=100*conteo_individual/palabras_totales #saca el porcentaje
print("el porcentaje es:", porcentaje,"%") #imprime todo


 