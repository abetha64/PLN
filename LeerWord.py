import re
from docx import Document

archivo_word = "Servidor_Streaming.docx" # Nombre del archivo de Word
doc = Document(archivo_word) # Leer el archivo de Word

# Obtener todo el texto del archivo de Word
texto_visible = ""
for paragraph in doc.paragraphs:
    texto_visible += paragraph.text + "\n"

print("Texto visible en el archivo de Word:")
print(texto_visible)

print ("====================================================================================================")

# Expresión regular para encontrar palabras de 3 a 5 letras entre espacios
expresion_regular = re.compile(r'\b\w{3,8}\b')

# Buscar palabras utilizando la expresión regular en el texto del archivo de Word
resultados_busqueda = expresion_regular.finditer(texto_visible)

print("Palabras encontradas:")
for resultado in resultados_busqueda:
    print(resultado.group(0))
