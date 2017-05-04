__author__ = 'graficos'
class Punto():

    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "Punto (%s, %s, %s)" %(self.x, self.y, self.z)
    def __repr__(self):
        return "Punto (%s, %s, %s)" %(self.x, self.y, self.z)


punto1 = Punto(1, 2, 3)
print(punto1)
print(repr(punto1))
print("####")
