num_a = int(input('Tamanho da lista A: '))
lista_a = []
num_b = int(input('Tamanho da lista B: '))
lista_b = []
i, j, t = 0, 0, 0
while i < num_a:
    num = int(input(f'Informe o {i + 1}° valor para a lista A: '))
    if lista_a.count(num) == 0:
        lista_a.append(num)
        i += 1
    else:
        print(f'O valor {num} já foi informado na lista A, informe outro não repetido.')
while j < num_b:
    num = int(input(f'Informe o {j + 1}° valor para a lista B: '))
    if lista_b.count(num) == 0:
        lista_b.append(num)
        j += 1
    else:
        print(f'O valor {num} já foi informado na lista A, informe outro não repetido.')
lista_r = lista_a.copy()
qtd = len(lista_b)
while t < qtd:
    if lista_r.count(lista_b[t]) == 0:
        lista_r.append(lista_b[t])
        t += 1
    else:
        t += 1
tam = len(lista_r)
print(f'São {tam} termos: {lista_r}')
