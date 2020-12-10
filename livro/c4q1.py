tamanho, i = 10, 0
lista = []
while i < tamanho:
    num = int(input(f'Informe o numero {i + 1} de {tamanho}: '))
    lista.append(num)
    i += 1
lista.reverse()
print(lista)
