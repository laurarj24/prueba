# TAREA 1 ==> Importar librerias

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

