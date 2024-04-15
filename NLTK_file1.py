<<<<<<< HEAD
import re
import requests
from bs4 import BeautifulSoup

url = input("Ingresa una URL por favor: ") #"https://latam.casadellibro.com/libros-ebooks-gratis/184"

respuesta = requests.get(url)
contenido_html = respuesta.text

soup = BeautifulSoup(contenido_html, 'html.parser') # Crear un objeto BeautifulSoup para analizar el HTML

texto_visible = soup.get_text()
print("Texto visible en la página web:")
print(texto_visible)

print ("====================================================================================================")

# Expresión regular para encontrar palabras de 3 o 4 letras entre espacios
expresion_regular = re.compile(r'\b\w{3,4}\b')

resultados_busqueda = expresion_regular.finditer(texto_visible)

for resultado in resultados_busqueda:
    print(resultado.group(0))
=======
import re
import requests
from bs4 import BeautifulSoup

url = "https://latam.casadellibro.com/libros-ebooks-gratis/184"

respuesta = requests.get(url)
contenido_html = respuesta.text

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(contenido_html, 'html.parser')

texto_visible = soup.get_text()
print("Texto visible en la página web:")
print(texto_visible)

print ("================================")

# Expresión regular para encontrar palabras de 3 o 4 letras entre espacios
expresion_regular = re.compile(r'\b\w{3,4}\b')

resultados_busqueda = expresion_regular.finditer(texto_visible)

for resultado in resultados_busqueda:
    print(resultado.group(0))
>>>>>>> 61994e8d4b625da5e1add7687086f4679169cde4
