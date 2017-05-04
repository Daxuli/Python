import random
import math
print("Juego de adivinar un entero dentro de un rango de valores")
# Definamos el rango de valores---------------------------------------------
rango = True
x = y = 0
while rango:
    x = input("introduce Limite Inferior LI:\n")
    y = input("introduce Limite Superior LS:\n")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Vslor introducido NO ES ENTERO, intente de nuevo")
        continue
    if x >= y:
        print("Limites incorrectos: LI > LS, intente de nuevo")
        continue
    rango = False
print("rango introducido: [%s-%s]" % (x, y))

# Empecemos el juego--------------------------------------------------------
max_attempts = math.floor(math.log2(y-x) + 1)
incognita = random.randint(x, y)
# print(incognita)  # Esta linea es para saber el numero durante pruebas

attempts = 0
while True:
    usuario = input("introduce un entero: [%s-%s]; intentos restantes: %s\n" % (x, y, max_attempts-attempts))
    try:
        usuario = int(usuario)
        attempts += 1
        if usuario == incognita:
            print("Correcto!")
            print(usuario)
            break
        elif usuario < incognita:
            print("Es mayor")
        else:
            print("Es menor")
    except ValueError:
        print("Vslor introducido NO ES ENTERO, intente de nuevo")
    if attempts == max_attempts:
        print("Game Over")
        break
