x, y, qtd_termos = 1, 0, 0
lista_pos, lista_neg = [], []
while x == 1:
    num_termos = int(input('Informe um número entre 0 e 50: '))
    if 0 <= num_termos <= 50:
        qtd_termos = num_termos
        x = 0
while y < qtd_termos:
    num = int(input('Informe um valor: '))
    if num < 0:
        lista_neg.append(num)
    else:
        lista_pos.append(num)
    y += 1
termos_neg = len(lista_neg)
termos_pos = len(lista_pos)
print(f'O número de termos informados foram:')
print(f'{termos_pos} - Positivos: {lista_pos}')
print(f'{termos_neg} - Negativos: {lista_neg}')
