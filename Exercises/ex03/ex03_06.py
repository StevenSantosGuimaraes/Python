# Forma 1:
contador1 = 1
mensagem1 = '--- Fim! ---'
while (contador1 <= 1000):
    vteste1 = contador1
    if(vteste1 % 2 == 0):
        print(contador1)
        contador1 += 1
    else:
        contador1 += 1
else:
    print(mensagem1)

# Forma 2:
contador2 = 1
mensagem2 = "--- End! ---"
for contador2 in range(1, 1001, +1):
    vteste2 = contador2
    if(vteste2 % 2 == 0):
        print(contador2)
        #contador2 += 1 // Linha dispensada
    else:
        contador2 += 1
else:
    print(mensagem2)