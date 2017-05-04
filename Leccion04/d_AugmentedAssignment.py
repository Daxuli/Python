i = 1
print(id(i), i)
i += 1  # equivalente a i = i + 1
print(id(i), i)
print("------------------------")

for _ in range(0, 3):
    i *= 2  # equivalente a i = i * 2
    print(id(i), i)

# augmented assignment