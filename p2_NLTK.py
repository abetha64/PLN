<<<<<<< HEAD
import nltk
import matplotlib.pyplot as plt
from matplotlib import rcParams

carpeta_nombre = "Documentos\\"
# archivo_nombre = "archivo_nuevo.txt"

with open(carpeta_nombre + "archivo_nuevo.txt", "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, language="spanish")
tokens_conjunto = set(tokens)
palabras_totales = len(tokens)
palabras_diferentes = len(tokens_conjunto)
print("Número total de palabras:", palabras_totales)
print("Número de palabras diferentes:", palabras_diferentes)

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto_nltk)

hapaxes = distribucion.hapaxes()
print("----------------------------------------------------------------------")
print("Palabras únicas (hapaxes):")
for hapax in hapaxes:
    print(hapax)

rcParams.update({"figure.autolayout": True})
plt.figure(figsize=(10, 6))
distribucion.plot(20, cumulative=False)  # muetra solo las 20 palabras más comunes
plt.title("Distribución de frecuencia de las 20 palabras más comunes")
plt.xlabel("Palabra")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

=======
import nltk
import matplotlib.pyplot as plt
from matplotlib import rcParams

carpeta_nombre = "Documentos\\"
# archivo_nombre = "archivo_nuevo.txt"

with open(carpeta_nombre + "archivo_nuevo.txt", "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, language="spanish")
tokens_conjunto = set(tokens)
palabras_totales = len(tokens)
palabras_diferentes = len(tokens_conjunto)
print("Número total de palabras:", palabras_totales)
print("Número de palabras diferentes:", palabras_diferentes)

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto_nltk)

hapaxes = distribucion.hapaxes()
print("----------------------------------------------------------------------")
print("Palabras únicas (hapaxes):")
for hapax in hapaxes:
    print(hapax)

rcParams.update({"figure.autolayout": True})
plt.figure(figsize=(10, 6))
distribucion.plot(20, cumulative=False)  # muetra solo las 20 palabras más comunes
plt.title("Distribución de frecuencia de las 20 palabras más comunes")
plt.xlabel("Palabra")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

>>>>>>> 61994e8d4b625da5e1add7687086f4679169cde4
