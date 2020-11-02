# Forma 1:
contador1 = 100
mensagem1 = '--- Fim! ---'
while (contador1 >= 0):
    print(contador1)
    contador1 -= 1
else:
    print(mensagem1)

# Forma 2:
contador2 = 100
mensagem2 = "--- End! ---"
for contador2 in range(100, -1, -1):
    print(contador2)
else:
    print(mensagem2)