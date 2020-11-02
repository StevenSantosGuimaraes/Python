# Forma 1:
texto1 = "Hello World!"
contador1 = 1
mensagem1 = '--- End! ---'
while (contador1 <= 100):
    print(contador1,'-',texto1)
    contador1 += 1
else:
    print(mensagem1)

# Forma 2:
texto2 = "Ola mundo!"
contador2 = 1
mensagem2 = '--- Fim! ---'
for contador2 in range(1, 101):
    print(contador2,"-",texto2)
    contador2 += 1
else:
    print(mensagem2)