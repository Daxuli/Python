midict = {1: "valor", "1": "otrovalor", "llave": list([1, 2, 3])}  # tambien es desordenado

print(type(midict), midict)
print(type(midict), midict[1])
print(type(midict), midict["llave"])
print("----------------")

miPuntero = midict["llave"]
miPuntero.append(1)
print(midict["llave"])
print("----------------")

# ----------------
print(midict.keys())
print(midict.items())
print("----------------")
for llave in midict.keys():
    print(midict[llave])
print("----------------")
for llave, valor in midict.items():  # podemos llamarlos al mismo tiempo porque tienen la misma estructura que items
    print(llave, valor)
print("----------------")

# ----------------
milista1 = [1, 2, 3]
milista2 = [3, 4, 5, 6]
milista3 = [7, 8, 9, 10, 11]

#  zip para empaquetar varias listas e iterar de golpe
for i, j, k in zip(milista2, milista1, milista3):
    print(i, j, k)
print("----------------")
for i in range(0, 3):  # recordatorio: llega hasta el 2
    print(milista3[i])
