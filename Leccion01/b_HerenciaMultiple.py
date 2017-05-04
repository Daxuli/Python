__author__ = 'graficos'

class Humano():
    def ataca(self):
        print("puñetazo")

class Ninja(Humano):
    def ataca(self):
        print("Shuriken")

class Cyborg(Humano):
    #def ataca(self):
    #   print("Laser")
    def defiende(self):
        print("escudo")
class T1000(Cyborg, Ninja):
    pass


Alvaro = T1000()
Alvaro.ataca()
print(T1000.__mro__) #Method Resolution Order

Andres = Cyborg()
Andres.ataca()