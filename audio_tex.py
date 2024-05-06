import pyaudio
import wave
import speech_recognition as sr
import pyttsx3

def grabar_audio(nombre_archivo, duracion):
    formato = pyaudio.paInt16
    canales = 1
    tasa_muestreo = 44100
    tamano_buffer = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(format=formato, channels=canales, rate=tasa_muestreo, input=True, frames_per_buffer=tamano_buffer)

    print("Grabando audio...la grabación durará 2 segundos...")

    frames = []

    for i in range(0, int(tasa_muestreo / tamano_buffer * duracion)):
        data = stream.read(tamano_buffer)
        frames.append(data)

    print("Grabación finalizada.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    archivo_salida = wave.open(nombre_archivo, 'wb')
    archivo_salida.setnchannels(canales)
    archivo_salida.setsampwidth(audio.get_sample_size(formato))
    archivo_salida.setframerate(tasa_muestreo)
    archivo_salida.writeframes(b''.join(frames))
    archivo_salida.close()

def convertir_audio_a_texto(nombre_archivo):
    reconocedor = sr.Recognizer()

    with sr.AudioFile(nombre_archivo) as fuente:
        audio = reconocedor.record(fuente)

    try:
        texto = reconocedor.recognize_google(audio, language='es-ES')
        print("Texto reconocido:")
        print(texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print("Error al solicitar resultados al servicio de reconocimiento de voz de Google: {0}".format(e))
    return None

def reproducir_texto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

nombre_archivo = input("Ingrese el nombre del archivo de audio a generar (incluya la extensión .wav): ")

duracion_grabacion = 2

grabar_audio(nombre_archivo, duracion_grabacion)
texto = convertir_audio_a_texto(nombre_archivo)
if texto:
    reproducir_texto(texto)
else:
    print("No se pudo reconocer el audio.")
