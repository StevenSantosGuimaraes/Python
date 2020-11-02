# Forma 1:
nvezes1 = int(input('Informe o número de repetições: '))
mtexto1 = str(input('Informe a mensagem a ser repetida: '))
contador1 = 1
mensagem1 = '--- Fim! ---'
while(contador1 <= nvezes1):
    print(mtexto1)
    contador1 += 1
else:
    print(mensagem1)

# Forma 2:
nvezes2 = int(input("Informe o número de vezes: "))
mtexto2 = str(input("Informe a mensagem: "))
contador2 = 1
mensagem2 = "--- End! ---"
for contador2 in range(0, nvezes2, +1):
    print(mtexto2)
else:
    print(mensagem2)