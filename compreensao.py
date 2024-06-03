# [expressão for elemento in lista if condição]
quadrados = [x**2 for x in range(1,6)]

print(quadrados)

quadrados2 = []
for x in range(1,6):
    quadrados.append(x**2)

print(quadrados2)

# FILTRAGEM DE ELEMENTOS
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

pares2 = []
for x in range(10):
    if x % 2 == 0:
        pares2.append(x)
    print(pares2)