import nltk
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from colorama import init, Fore, Style
from docx import Document

init()

def leer_archivo_docx(archivo_docx):
    doc = Document(archivo_docx)
    texto = ""
    for paragraph in doc.paragraphs:
        texto += paragraph.text + "\n"
    return texto

def guardar_texto_en_archivo(texto, filename='texto_extraido.txt'):
    with open(filename, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)
    print(f"Se ha guardado el contenido en '{filename}'")

def contar_palabras_lineas(texto):
    numero_palabras = len(texto.split())
    numero_lineas = len(texto.split('\n'))
    print(">>Número de palabras:", numero_palabras)
    print(">>Número de líneas:", numero_lineas)

def mostrar_palabras_cortas(texto):
    palabras_3_4_caracteres = [palabra for palabra in texto.split() if len(palabra) in [3, 4]]
    print(Fore.YELLOW +"Palabras de 3 o 4 caracteres:", palabras_3_4_caracteres)

def buscar_palabra(texto, palabra):
    # Contar el número de veces que aparece la palabra
    numero_apariciones = texto.lower().count(palabra.lower())
    print("La palabra '{}' aparece {} veces en el texto.".format(palabra, numero_apariciones))

def limpiar_texto(texto):
    # Tokenizar el texto y eliminar palabras funcionales
    palabras_funcionales = set(stopwords.words("spanish"))
    tokens = word_tokenize(texto, "spanish")
    tokens_limpios = [token for token in tokens if token not in palabras_funcionales]
    print("Tokens: ", len(tokens))
    print("Tokens limpios: ", len(tokens_limpios))
    return tokens_limpios

def graficar_distribucion_frecuencia(tokens_limpios):
    texto_nltk = nltk.Text(tokens_limpios)
    # Calcular la distribución de frecuencia
    distribucion_frecuencia = texto_nltk.vocab()
    # Graficar las 40 palabras más comunes
    plt.figure(figsize=(10, 6))
    texto_nltk.plot(40)
    plt.show()

def main():
    archivo_word = input(Fore.MAGENTA + "Ingresa el nombre del archivo de Word (incluye la extensión .docx): " + Style.RESET_ALL)
    texto_archivo = leer_archivo_docx(archivo_word)

    print("Contenido del archivo de Word:")
    print(texto_archivo)
    print(Fore.RED + "--------------------------------------------------------------------------------" + Style.RESET_ALL)

    pregunta = input(Fore.MAGENTA + "¿Desea guardar el contenido en un archivo de texto? (s/n) R = " + Style.RESET_ALL)
    if pregunta.lower() == "s":
        archivo_txt = input(Fore.GREEN + "Ingresa el nombre del archivo de texto de salida (incluye la extensión .txt): " + Style.RESET_ALL)
        guardar_texto_en_archivo(texto_archivo, archivo_txt)
    elif pregunta.lower() == "n":
        print(Fore.RED + "Continuando con el contenido del archivo de Word...!!" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + "Opción no válida. Continuando con el contenido del archivo de Word..."+ Style.RESET_ALL)

    contar_palabras_lineas(texto_archivo)
    mostrar_palabras_cortas(texto_archivo)
    palabra_buscar = input(Fore.BLUE + "Ingresa la palabra que deseas buscar en el texto: " + Style.RESET_ALL)
    buscar_palabra(texto_archivo, palabra_buscar)
    tokens_limpios = limpiar_texto(texto_archivo)
    graficar_distribucion_frecuencia(tokens_limpios)

if __name__ == "__main__":
    main()
