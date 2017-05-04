milista = list(range(0, 11))
milista.extend(milista)
print(milista)
print("-------------------------------------------")

# --------------------------------------------------------------------------------
numerospares1 = list()
numerospares2 = ["", ]*7
numerospares3 = [1, ]*7
numerospares4 = [[], ]*7

print(type(numerospares1), numerospares1)
print(type(numerospares2), numerospares2)
print(type(numerospares3), numerospares3)
print(type(numerospares4), numerospares4)
print("-------------------------------------------")

# --------------------------------------------------------------------------------
for elem in milista:
    if elem % 2 == 0:
        numerospares1.append(elem)
print(numerospares1)

n_par1 = [elem for elem in milista if (elem % 2 == 0)]  # lista
n_par2 = (elem for elem in milista if (elem % 2 == 0))  # tupla
n_par3 = {elem for elem in milista if (elem % 2 == 0)}  # set

print(type(n_par1), n_par1)
print(type(n_par2), n_par2)
print(type(n_par3), n_par3)
print("-------------------------------------------")

# --------------------------------------------------------------------------------
for elem1, elem2, elem3, in zip(n_par1, n_par2, n_par3):  # para con el set
    print(elem1, elem2, elem3)
