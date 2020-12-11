num_min = int(input('Informe um valor: '))
num_max = int(input(f'Informe outro valor maior que {num_min}: '))
i = 0
lista_div, lista_n_div = [], []
while num_max <= num_min:
    num_max = int(input(f'Valor {num_max} informado não é válido, informe outro maior que {num_min}: '))
i = num_min
while i <= num_max:
    if i % 7 == 0 and i != 0:
        lista_div.append(i)
        i += 1
    else:
        lista_n_div.append(i)
        i += 1
print(f'{len(lista_div)} - Divisores de 7: {lista_div}')
print(f'{len(lista_n_div)} - Não divisores de 7: {lista_n_div}')
