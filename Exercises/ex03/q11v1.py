qtd_ler = int(input('Quantos números deseja ler? '))
vlr_temp, vlr_soma, vlr_media, i = 0, 0, 0, 0
for i in range(0, qtd_ler):
    vlr_temp = float(input(f'Informe o {i + 1}º número: '))
    vlr_soma += vlr_temp
vlr_media = vlr_soma / (i + 1)
print(f'A soma dos {i + 1} valores informados totalizam {vlr_soma} e a média é {vlr_media}.')
