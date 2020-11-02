listagem = []
contador = 0
indice = 0
maisvelho = ''
ntermos = int(input('Número de registros:'))
for contador in range(0, ntermos):
    novonome = input('Nome:')
    novaidade = int(input('Idade:'))
    if contador == 0 or novaidade > listagem[-1]:
        listagem.append(novaidade)
        maisvelho = novonome
    else:
        indice = 0
        while indice < len(listagem):
            if novaidade <= listagem[indice]:
                listagem.insert(indice, novaidade)
                maisvelho = novonome
                break
            indice += 1
print('A pessoa com maior idade é:', maisvelho,'com:',listagem[-1])