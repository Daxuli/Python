#Como generar documentacion
class Persona():
    """
    Pantilla de la clase Persona

    instancia  = Persona(nombre)
    """
    def __init__(self,nombre):
        self.nombre = nombre #asignacion del nombre  al atributo nombre

    def saludo(self):
        """
    funcion que hace saludar a la persona
        """
        print("hola soy una Persona")

Jessica = Persona("Jessica")
print(Jessica.__doc__)
print(Jessica.saludo.__doc__)
