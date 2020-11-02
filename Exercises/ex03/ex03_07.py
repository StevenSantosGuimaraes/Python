# Forma 1:
contador1 = 1000
mensagem1 = '--- Fim! ---'
while (contador1 >= 0):
    vteste1 = contador1
    if(vteste1 % 2 == 1):
        print(contador1)
        contador1 -= 1
    else:
        contador1 -= 1
else:
    print(mensagem1)

# Forma 2:
contador2 = 1000
mensagem2 = "--- End! ---"
for contador2 in range(1000, 0, -1):
    vteste2 = contador2
    if(vteste2 % 2 == 1):
        print(contador2)
    else:
        contador2 -= 1
else:
    print(mensagem2)