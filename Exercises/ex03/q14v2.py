num, maior_num, menor_num, i = 0, 0, 0, 0
while i < 10:
    num = int(input(f'Informe o {i + 1}º número: '))
    if i == 1:
        maior_num = num
        menor_num = num
    else:
        if num < menor_num:
            menor_num = num
        if num > maior_num:
            maior_num = num
    i += 1
print(f'O menor valor digitado foi {menor_num} e o maior foi {maior_num}.')

