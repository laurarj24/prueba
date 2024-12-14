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
    "¿Cuál es el único número primo par?": "2",
    "¿Qué científico descubrió el principio de incertidumbre en la mecánica cuántica?": "Werner Heisenberg",
    "¿Qué filósofo griego fue maestro de Alejandro Magno?": "Aristóteles",
    "¿Cuál es el idioma con más hablantes nativos en el mundo?": "Chino mandarín",
    "¿Qué metal se conoce como 'el metal del diablo' debido a su toxicidad?": "Mercurio",
    "¿Qué escritor ruso escribió *Crimen y castigo*?": "Fiódor Dostoyevski",
    "¿Cuál es el único mamífero capaz de volar?": "Murciélago",
    "¿Cómo se llama el punto matemático donde dos curvas se encuentran pero no cruzan?": "Punto de tangencia",
    "¿Cuál es el órgano más pequeño del cuerpo humano?": "El estapedio (en el oído)",
    "¿Qué país tiene el mayor número de husos horarios del mundo?": "Francia (incluyendo territorios de ultramar)",
    "¿Cómo se llama el proceso por el cual las células convierten glucosa en energía?": "Respiración celular",
    "¿Qué emperador romano legalizó el cristianismo con el Edicto de Milán?": "Constantino I",
    "¿Qué arquitecto diseñó la Sagrada Familia en Barcelona?": "Antoni Gaudí",
    "¿Cuál es la constante matemática representada por la letra 'e'?": "2.718",
    "¿Cómo se llama el estudio de los mapas antiguos?": "Cartografía histórica",
    "¿Cuál es el término técnico para los planetas fuera del sistema solar?": "Exoplanetas",
    "¿Qué gen se conoce como 'el gen maestro' responsable del desarrollo del ojo?": "PAX6",
    "¿Qué río atraviesa 10 países, más que cualquier otro río del mundo?": "El Danubio",
    "¿Cómo se llama la medida de la resistencia del agua a fluir?": "Viscosidad",
    "¿Qué científico introdujo el concepto de 'entropía' en la termodinámica?": "Rudolf Clausius",
}
