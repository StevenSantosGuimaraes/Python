texto1 = "Hello World"
contador1 = 1
tFinal1 = "--- Fim! ---"

# print(texto * 10) // Forma direta

# Forma 1:
while (contador1 <= 10):
    print(texto1, end=" / ")
    contador1 += 1
else:
    print(tFinal1)

# Forma 2:
texto2 = "Olá mundo"
contador2 = 1
tFinal2 = "--- End! ---"
for contador2 in range(10):
    print(texto2, end=' / ')
    contador2 += 1
else:
    print(tFinal2)