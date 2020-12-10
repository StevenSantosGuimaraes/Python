qtd_ler = int(input('Quantos números deseja ler? '))
vlr_temp, vlr_soma, vlr_media, i = 0, 0, 0, 0
while i < qtd_ler:
    vlr_temp = float(input(f'Informe o {i + 1}º número: '))
    vlr_soma += vlr_temp
    i += 1
vlr_media = vlr_soma / (i)
print(f'A soma dos {i} valores informados totalizam {vlr_soma} e a média é {vlr_media}.')
