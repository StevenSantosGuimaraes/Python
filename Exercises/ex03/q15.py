listagem = []
analisador = 1
while analisador != 0:
    nNum = int(input('Informe um número inteiro DIFERENTE de ZERO para CONTINUAR ou ZERO para PARAR: '))
    if nNum != 0:
        listagem.append(nNum)
        continue
    elif nNum == 0:
        break
    else:
        continue
print(f'Os valores informados foram: {listagem}')
verificador = 1
while verificador != 0:
    verificador = 0
    indice = 0
    while indice < (len(listagem) - 1):
        if listagem[indice] > listagem[indice + 1]:
            listagem[indice], listagem[indice + 1] = listagem[indice + 1], listagem[indice]
            verificador = 1
        indice += 1
print(f'Lista orgenada: {listagem}')
