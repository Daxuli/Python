__author__ = 'graficos'



class CajaFuerte():
    def __init__(self,secreto, PIN):#protegidas
        self.secreto = secreto#visibles
        self._secreto = self.secreto#privadas
        self.__PIN = PIN#ocultas

micajafuerte = CajaFuerte("le gusta mas FORTRAN", "0000")

print(micajafuerte._secreto)
micajafuerte.secreto = "ademas en Notepard"
print(micajafuerte._secreto)

print(micajafuerte._CajaFuerte__PIN)