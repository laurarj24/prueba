# TAREA 1 ==> Importar librerias
import re
import random
import tkinter as tk
# TAREA 2 ==> Desarrollar funcion que ejecute el juego
def verificacion_pregunta(diccionario):

    vidas = 5
    aciertos = 0
    while vidas > 0 and aciertos < 3:
        # seleccionamos la pregunta
        pregunta = random.choice(list(diccionario)) #Generamos una lista con las claves 
        #(preguntas) del diccionario y seleccionamos una de manera aleatoria. Lo 
        #almacenamos en la variable 'pregunta'
        respuesta = input(f"Dinos tu respuesta a la pregunta ==> {pregunta}")
        if diccionario[pregunta].lower() == respuesta.lower():
            aciertos += 1
            print(f"Enhorabuena! Respuesta acertada")
        else: 
            vidas -= 1
            print(f"Vaya... fallaste!! sigue intentandolo, el total de oportunidades que te quedan es {vidas}")
        diccionario.pop(pregunta) # para que la misma pregunta no vuelva a salir dos veces 

    if aciertos == 3:
        return f"¡¡¡VICTORIA!!!"
    else:
        return f"¡¡¡DERROTA!!!"
# TAREA 3 ==> Hacer los diccionarios de preguntas y respuestas

preguntas = {
    "¿Cuál es la capital de Canadá?": "Ottawa",
    "¿Qué montaña es la más alta del mundo?": "Monte Everest",
    "¿Qué número romano representa el 50?": "L",
    "¿Qué elemento tiene el número atómico 1?": "Hidrógeno",
    "¿Quién fue el primer hombre en pisar la Luna?": "Neil Armstrong",
    "¿En qué continente se encuentra el desierto del Sahara?": "África",
    "¿Qué compositor alemán quedó sordo y aún así compuso la Novena Sinfonía?": "Ludwig van Beethoven",
    "¿Cómo se llama el triángulo con dos lados iguales?": "Isósceles",
    "¿Cuál es el libro más vendido del mundo después de la Biblia?": "Don Quijote de la Mancha",
    "¿Qué río es el más largo del mundo?": "Río Amazonas",
}