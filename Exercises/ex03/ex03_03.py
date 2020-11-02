# Forma 1:
contador1 = 1
mensagem1 = '--- Fim! ---'
while (contador1 <= 100):
    print(contador1)
    contador1 += 1
else:
    print(mensagem1)

# Forma 2:
contador2 = 1
mensagem2 = '--- End! ---'
for contador2 in range(1, 101):
    print(contador2)
    contador2 += 1
else:
    print(mensagem2)