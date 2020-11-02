# Forma 1:
numvezes1 = int(input('Informe a quantidade de vezes da repetição: '))
texto1 = "Hello World!"
contador1 = 1
mensagem1 = "--- Fim! ---"
while (contador1 <= numvezes1):
    print(texto1)
    contador1 += 1
else:
    print(mensagem1)

# Forma 2:
numvezes2 = int(input("Informe a quantidade de repetições: "))
texto2 = 'Olá mundo!'
contador2 = 1
mensagem2 = '--- End! ---'
for contador2 in range(0, numvezes2):
    print(texto2)
    contador2 += 1
else:
    print(mensagem2)