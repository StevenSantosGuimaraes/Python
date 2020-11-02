listagem = []
contador = 0
indice = 0
sIdadeF = 0
sIdadeM = 0
sQuantF = 0
sQuantM = 0
nRegistros = int(input('Número de registros:'))
for contador in range(0, nRegistros):
    nNome = input('Nome: ')
    nGenero = str(input('Informe o sexo (M/F): '))
    nIdade = int(input('Idade: '))
    print('----- // -----')
    if contador == 0 or nIdade > listagem[-1]:
        listagem.append(nIdade)
        if((nGenero == 'f') or (nGenero == 'F')):
            sIdadeF += nIdade
            sQuantF += 1
        elif((nGenero == 'm') or (nGenero == 'M')):
            sIdadeM += nIdade
            sQuantM += 1
    else:
        indice = 0
        while indice < len(listagem):
            if nIdade <= listagem[indice]:
                listagem.insert(indice, nIdade)
                if ((nGenero == 'f') or (nGenero == 'F')):
                    sIdadeF += nIdade
                    sQuantF += 1
                elif ((nGenero == 'm') or (nGenero == 'M')):
                    sIdadeM += nIdade
                    sQuantM += 1
                break
            indice += 1
mIdadeF = (sIdadeF / sQuantF)
mIdadeM = (sIdadeM / sQuantM)
print('A média de idade informada do público feminino é:', mIdadeF,'e masculino:',mIdadeM)