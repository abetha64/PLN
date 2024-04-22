import os
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from colorama import init, Fore, Style
from docx import Document
import PyPDF2

init()
nltk.download('stopwords')

def validar_nombre_archivo(archivo):
    if os.path.exists(archivo):
        return True
    else:
        print(Fore.RED + "El archivo no existe.")
        return False

def leer_archivo_pdf(archivo_pdf):
    try:
        with open(archivo_pdf, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            texto = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texto += page.extract_text()
            return texto
    except Exception as e:
        print(Fore.RED + "Error al leer el archivo PDF:", e)
        return None

def guardar_texto_en_archivo(texto, filename='texto_extraido.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as archivo:
            archivo.write(texto)
        print(f"Se ha guardado el contenido en '{filename}'")
    except Exception as e:
        print(Fore.RED + "Error al guardar el archivo de texto:", e)

def contar_palabras_lineas(texto): 
    try:
        numero_palabras = len(texto.split())
        numero_lineas = len(texto.split('\n'))
        print(">>Número de palabras:", numero_palabras)
        print(">>Número de líneas:", numero_lineas)
    except Exception as e:
        print(Fore.RED + "Error al contar palabras y líneas:", e)

def mostrar_palabras_cortas(texto):
    try:
        palabras_3_4_caracteres = [palabra for palabra in texto.split() if len(palabra) in [3, 4]]
        print(Fore.YELLOW +"Palabras de 3 o 4 caracteres:", palabras_3_4_caracteres)
    except Exception as e:
        print(Fore.RED + "Error al mostrar palabras cortas:", e)

def buscar_palabra(texto, palabra):
    try:
        # Contar el número de veces que aparece la palabra
        numero_apariciones = texto.lower().count(palabra.lower())
        print("La palabra '{}' aparece {} veces en el texto.".format(palabra, numero_apariciones))
    except Exception as e:
        print(Fore.RED + "Error al buscar la palabra:", e)

def limpiar_texto(texto):
    try:
        # Tokenizar el texto y eliminar palabras funcionales
        palabras_funcionales = set(stopwords.words("spanish"))
        tokens = word_tokenize(texto, "spanish")
        tokens_limpios = [token for token in tokens if token not in palabras_funcionales]
        print("Tokens: ", len(tokens))
        print("Tokens limpios: ", len(tokens_limpios))
        return tokens_limpios
    except Exception as e:
        print(Fore.RED + "Error al limpiar el texto:", e)
        return []

def graficar_distribucion_frecuencia(tokens_limpios):
    try:
        texto_nltk = nltk.Text(tokens_limpios)
        distribucion_frecuencia = texto_nltk.vocab()
        plt.figure(figsize=(10, 6))
        texto_nltk.plot(20)
        plt.show()
    except Exception as e:
        print(Fore.RED + "Error al graficar la distribución de frecuencia:", e)

def main():
    try:
        archivo_pdf = input(Fore.MAGENTA + "Ingresa el nombre del archivo PDF (incluye la extensión .pdf): " + Style.RESET_ALL)
        
        while not validar_nombre_archivo(archivo_pdf):
            archivo_pdf = input(Fore.MAGENTA + "Ingresa el nombre del archivo PDF (incluye la extensión .pdf): " + Style.RESET_ALL)

        texto_archivo = leer_archivo_pdf(archivo_pdf)

        if texto_archivo:
            print("Contenido del archivo PDF:")
            print(texto_archivo)
            print(Fore.RED + "--------------------------------------------------------------------------------" + Style.RESET_ALL)

            pregunta = input(Fore.MAGENTA + "¿Desea guardar el contenido en un archivo de texto? (s/n) R = " + Style.RESET_ALL)
            
            if pregunta.lower() == "s":
                archivo_txt = input(Fore.GREEN + "Ingresa el nombre del archivo de texto de salida (incluye la extensión .txt): " + Style.RESET_ALL)
                guardar_texto_en_archivo(texto_archivo, archivo_txt)
            elif pregunta.lower() == "n":
                print(Fore.RED + "Continuando con el contenido del archivo de PDF...!!" + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "Opción no válida. Continuando con el contenido del archivo de PDF..."+ Style.RESET_ALL)

            contar_palabras_lineas(texto_archivo)
            mostrar_palabras_cortas(texto_archivo)
            palabra_buscar = input(Fore.BLUE + "Ingresa la palabra que deseas buscar en el texto: " + Style.RESET_ALL)
            buscar_palabra(texto_archivo, palabra_buscar)
            tokens_limpios = limpiar_texto(texto_archivo)
            graficar_distribucion_frecuencia(tokens_limpios)
    except KeyboardInterrupt:
        print(Fore.RED + "\nSe ha interrumpido el programa." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "Error:", e)
        opcion = input(Fore.MAGENTA + "¿Desea continuar? (s/n) R = " + Style.RESET_ALL)
        if opcion.lower() != "s":
            print(Fore.RED + "Saliendo del programa..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
