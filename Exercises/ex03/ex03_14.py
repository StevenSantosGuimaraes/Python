listagem = []
contador = 1
for contador in range(0, 10):
    minicont = contador + 1
    novoRegistro = int(input(f'Informe o {minicont}º termo: '))
    listagem.append(novoRegistro)
print("A sequencia informada foi: ", listagem)
trocou = 1
while trocou:
    trocou = 0
    indice = 0
    while indice < (len(listagem) - 1):
        if listagem[indice] > listagem[indice + 1]:
            listagem[indice], listagem[indice + 1] = listagem[indice +1], listagem[indice]
            trocou = 1
        indice += 1
    print("Passo a passo da realocação: ",listagem)
print("Lista orgenada: ", listagem)
print("O menor número é:",listagem[0])
print("O maior número é:",listagem[-1])