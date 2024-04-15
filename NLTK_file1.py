import re
import requests
from bs4 import BeautifulSoup

url = "https://classroom.google.com/c/NjYxMDgwMjE1OTU4/a/NjI4NzMyMzAwNzY4/details"

respuesta = requests.get(url)
contenido_html = respuesta.text

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(contenido_html, 'html.parser')
# Extraer el texto visible de la página web
texto_visible = soup.get_text()

# Expresión regular para encontrar palabras de 3 o 4 letras entre espacios
expresion_regular = re.compile(r'\b\w{3,4}\b')

resultados_busqueda = expresion_regular.finditer(texto_visible)

for resultado in resultados_busqueda:
    print(resultado.group(0))
