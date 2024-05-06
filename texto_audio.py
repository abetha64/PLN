import pyttsx3
import os
import docx

def texto_a_audio(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de reproducción del audio (opcional)
    engine.save_to_file(texto, 'audio_generado3.mp3')
    engine.runAndWait()

def leer_archivo_texto(archivo):
    extension = os.path.splitext(archivo)[1] #validacioin de archivos
    if extension == '.txt':
        with open(archivo, 'r', encoding='utf-8') as f:
            texto = f.read()
        return texto
    elif extension == '.docx':
        doc = docx.Document(archivo)
        texto = ''
        for paragraph in doc.paragraphs:
            texto += paragraph.text + '\n'
        return texto
    else:
        print("Formato de archivo no compatible.")

def main():
  
    nombre_archivo = input("Ingrese el nombre del archivo (incluya la extensión .txt o .docx): ")
    texto = leer_archivo_texto(nombre_archivo)

    if texto:
        texto_a_audio(texto)
        print("Texto convertido a audio y reproducido.")
    else:
        print("No se pudo leer el archivo.")

if __name__ == "__main__":
    main()
