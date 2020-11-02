# Forma 1:
contador1 = 1
somador1 = 0
while (contador1 <= 100):
    somador1 += contador1
    contador1 += 1
else:
    print(somador1)

# Forma 2:
contador2 = 1
somador2 = 0
for contador2 in range(1, 101, +1):
    somador2 += contador2
    #contador2 += 1 // Dispensado
else:
    print(somador2)