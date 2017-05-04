mitupla = (1, 2, 3)  # no hacen falta los parentesis (aunque facilitan la lectura)
mitupla2 = tuple((1, 2, 3))
mitupla3 = tuple([1, 2, 3])

print(id(mitupla), type(mitupla), mitupla)
print(id(mitupla2), type(mitupla2), mitupla2)
print(id(mitupla3), type(mitupla3), mitupla3)
print("---------------------------")

# ------------------------mutable-inmutable
milista = [1, 2]
print(id(milista), type(milista), milista)
milista.clear()
print(id(milista), type(milista), milista)  # se mantiene el mismo id
milista.extend([1, 2, 3])
print(id(milista), type(milista), milista)  # tambien
milista = [1, 2, 3]
print(id(milista), type(milista), milista)  # en cambio si lo hacemos asi, si que cambia el id

# mitupla.extend(3)  #esta linea no tiene sentido. Las tuplas no tienen estos atributos, no se pueden modificar
mitupla = 1,   # al ser inmutable, se rompe la primera tupla y se le asigna un nuevo id a mitupla
mitupla4 = 1, 2  # para optimizar el proceso(?), reutiliza el id que ya no sirve de mitupla
milista2 = [1, 2, 3]  # coge el id antiguo de milista

print(id(mitupla), type(mitupla), mitupla)
print(id(mitupla4), type(mitupla4), mitupla4)
print(id(milista2), type(milista2), milista2)
print("---------------------------")

# -----------------------------sets
miset = {2, 2, 1, 1, 1, 1, "1"}
print(id(miset), type(miset), miset)  # ojo, no estan ordenados
