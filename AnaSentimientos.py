#EN ESTE PROGRAMA ARROJA EL SCORE DE LA POLARIDAD DEL SENTIMIENTO

from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator


# Crear un analizador de intensidad de sentimiento
ola = SentimentIntensityAnalyzer()

def traducir_to_eng(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='en').text
    return translated_text

# Frase a evaluar
#frase = "llorar por ti" #frase en español
frase=input("Favor de introducir una frase a analizar_____________")
frase_en = traducir_to_eng(frase) #la traaduce a inglés

sentimiento = ola.polarity_scores(frase_en) #analiza la polaridad de la frase dada

print("Frase original:", frase)
print("Frase traducida al inglés:", frase_en)
print("Puntuación de sentimiento:", sentimiento)


# EN ESTE SOLAMENTE ARROJA EL SENTIMIENTO, SIN POLARIDAD
# from nltk.sentiment import SentimentIntensityAnalyzer
# from googletrans import Translator

# # Crear un analizador de intensidad de sentimiento
# ola = SentimentIntensityAnalyzer()

# def translate_to_english(text):
#     translator = Translator()
#     translated_text = translator.translate(text, dest='en').text
#     return translated_text

# # Frase a evaluar
# frase = "NLTK es una excelente biblioteca para procesamiento de lenguaje natural."
# frase= input("Ingresa una frase a evaluar:________:")

# # Traducir la frase a inglés
# frase_en = translate_to_english(frase)

# # Analizar el sentimiento de la frase traducida
# sentimiento = ola.polarity_scores(frase_en)

# # Obtener la clasificación de sentimiento
# if sentimiento['compound'] >= 0.05:
#     clasificacion = "Positivo"
# elif sentimiento['compound'] <= -0.05:
#     clasificacion = "Negativo"
# else:
#     clasificacion = "Neutral"

# # Mostrar la clasificación de sentimiento
# print("Frase original:", frase)
# print("Frase traducida:", frase_en)
# print("Clasificación de sentimiento:", clasificacion)

