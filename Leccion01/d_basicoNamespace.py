class Persona():

    def __init__(self,nombre):
        self.nombre = nombre

    def saludo(self):

        print("hola soy una Persona")
        return "Greetings"
Juan = Persona("Juan")

print(Juan.saludo())
print(Juan.saludo)
print(id(Juan.saludo))

print(Juan)
print(id(Juan))

Alberto = Juan
print(Alberto)
print(id(Alberto))

Alberto.nombre = "Alberto"
print("Juan: Soy " + Juan.nombre)