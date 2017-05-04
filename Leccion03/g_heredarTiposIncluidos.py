class ListaHabladora(list):
    def append(self, p_object):
        print("Estoy añadiento ", str(p_object))
        super(ListaHabladora, self).append(p_object)

l1 = ListaHabladora([1, 2, 3])
l1.append("elemento")
print(l1)
print("--------")
# ---------


class MiEntero(int):
    def __add__(self, other):
        return 42  # estamos modificando el comportamiento de + de la clase "MiEntero" para que el resultado salga 42

i1 = MiEntero(0)
print(i1 + i1)
print(i1 + 1)
print(1 + i1)

print("--------")
print(3*"a")
