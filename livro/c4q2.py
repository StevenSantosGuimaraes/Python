lista1, lista2 = [], []
tam1, tam2 = 10, 10
i, j = 0, 0
while i < tam1:
    lista1.append(int(input(f'Informe o valor {i + 1}º da lista 1: ')))
    i += 1
while j < tam2:
    lista2.append(int(input(f'Informe o valor {j + 1}º da lista 2: ')))
    j += 1
lista3 = lista1 + lista2
print(lista3)
