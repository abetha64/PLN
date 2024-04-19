import nltk
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from colorama import init, Fore, Style

init()

def obtener_contenido_pagina(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.content
    else:
        print(Fore.RED + 'Error al obtener la página:', respuesta.status_code)
        return None

def extraer_texto_pagina(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    parrafos = soup.find_all('p')
    return ' '.join([parrafo.get_text() for parrafo in parrafos])

def guardar_texto_en_archivo(texto, filename='texto_extraido.txt'):
    with open(filename, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

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
    salida = False
    while not salida:
        pregunta = input(Fore.MAGENTA + "¿Desea ingresar una URL personalizada? (s/n) R = " + Style.RESET_ALL)
        if pregunta.lower() == "s":
            liga = input(Fore.GREEN +"Ingresa la URL de la página web a analizar: "+ Style.RESET_ALL)
            salida = True
        elif pregunta.lower() == "n":
            liga = 'https://latam.casadellibro.com/libros-ebooks-gratis/184'
            salida = True
        else:
            salida = False

    contenido_pagina = obtener_contenido_pagina(liga)
    if contenido_pagina:
        texto_pagina = extraer_texto_pagina(contenido_pagina)
        guardar_texto_en_archivo(texto_pagina)
        contar_palabras_lineas(texto_pagina)
        mostrar_palabras_cortas(texto_pagina)
        palabra_buscar = input(Fore.BLUE + "Ingresa la palabra que deseas buscar en el texto: "+ Style.RESET_ALL)
        buscar_palabra(texto_pagina, palabra_buscar)
        tokens_limpios = limpiar_texto(texto_pagina)
        graficar_distribucion_frecuencia(tokens_limpios)

if __name__ == "__main__":
    main()
