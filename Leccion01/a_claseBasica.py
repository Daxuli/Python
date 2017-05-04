__author__ = 'graficos'
#Con el simbolo # incluye 1 linea de comentario

"""
La otra opcion es generar un string
si lo quiero
"""
# Voy a generar mi primera clase vacia
class MiPrimeraClase:
    pass #pass es 1 palabra clave para rellenar el bloque

#Voy a definir una funcion
def misaludo():
    print("Hola")
# Voy a generar mi primera clase
class Persona():
    def __init__(self,nombre):
        self.nombre = nombre
    def saludo(self):
        print("hola soy una Persona")

misaludo()
Sergio = Persona("Sergio")
Sergio.saludo()

class Alumno(Persona):
    def saludo(self):
        print("Hola, soy "+self.nombre)

Daniel = Alumno("Daniel")
Daniel.saludo()