idadeSala = []
analisador = 1
tIdade = 0
while(analisador != 0):
    nIdade = int(input("Uma idade válida para continua ou ZERO para iniciar analise: "))
    if(nIdade != 0):
        idadeSala.append(nIdade)
        tIdade += nIdade
        nIdade = 0
        continue
    elif(nIdade == 0):
        break
    else:
        continue
print("Os valores informados foram: ", idadeSala)
verificador = 1
while verificador != 0:
    verificador = 0
    indice = 0
    while indice < (len(idadeSala) - 1):
        if idadeSala[indice] > idadeSala[indice + 1]:
            idadeSala[indice], idadeSala[indice + 1] = idadeSala[indice + 1], idadeSala[indice]
            verificador = 1
        indice += 1
i = 0
cont18 = 0
nTermos = len(idadeSala)
media = tIdade / nTermos
mediana = 0
while i < (len(idadeSala) - 1):
    if idadeSala[i] >= 18:
        cont18 += 1
        i += 1
    else:
        i += 1
k = len(idadeSala)
if(nTermos % 2 == 0):
    j = int(k / 2)
    mediana = (idadeSala[j - 1] + idadeSala[j]) / 2
else:
    j = int((k - 1) / 2)
    mediana = idadeSala[j]
print(f"Lista orgenada: {idadeSala}, a média de idade é: {media} anos e a mediana é: {mediana} anos.")