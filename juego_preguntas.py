# TAREA 3 ==> Hacer los diccionarios de preguntas y respuestas

preguntas_faciles = {
    "¿Cuál es la capital de Canadá?": "Ottawa",
    "¿Qué planeta es conocido como el Planeta Rojo?": "Marte",
    "¿En qué año comenzó la Segunda Guerra Mundial?": "1939",
    "¿Cuál es el símbolo químico del oro?": "Au",
    "¿Quién pintó La Última Cena?": "Leonardo da Vinci",
    "¿Qué océano es el más grande del mundo?": "Océano Pacífico",
    "¿Quién escribió *Don Quijote de la Mancha*?": "Miguel de Cervantes",
}

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

print("Cambio 2")

