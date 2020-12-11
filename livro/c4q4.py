n_numeros = int(input('Quantos números devo ler? '))
lista = []
i = 0
while i < n_numeros:
    num = int(input(f'Digite o {i + 1}º número: '))
    if lista.count(num) == 0:
        lista.append(num)
        i += 1
    else:
        print('O número informado já está salvo. Informe outro.')
print(lista)
