# TAREA 1 ==> Importar librerias
import re
import random
import tkinter as tk

# TAREA 2 ==> Desarrollar funcion que ejecute el juego

# TAREA 3 ==> Hacer los diccionarios de preguntas y respuestas

preguntas = {
    "¿Cuál es la capital de Canadá?": "Ottawa",
    "¿Qué planeta es conocido como el Planeta Rojo?": "Marte",
    "¿En qué año comenzó la Segunda Guerra Mundial?": "1939",
    "¿Cuál es el símbolo químico del oro?": "Au",
    "¿Quién pintó La Última Cena?": "Leonardo da Vinci",
    "¿Qué océano es el más grande del mundo?": "Océano Pacífico",
    "¿Quién escribió *Don Quijote de la Mancha*?": "Miguel de Cervantes",
    "¿Qué país tiene forma de bota en el mapa?": "Italia",
    "¿Cómo se llama la molécula que contiene la información genética?": "ADN",
    "¿Cuántos jugadores hay en un equipo de baloncesto en la cancha?": "Cinco",
    "¿Cuál es el idioma oficial de Brasil?": "Portugués",
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
