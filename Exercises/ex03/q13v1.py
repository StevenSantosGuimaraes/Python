qtd_registros = int(input('Quantos registros devo realizar? '))
idade, med_idade_f, med_idade_m, t_idade_f, t_idade_m = 0, 0, 0, 0, 0
qtd_m, qtd_f, i = 0, 0, 0
sexo = ''
for i in range(0, qtd_registros):
    sexo = str(input(f'Informe o sexo do {i+1}° indivíduo [F/M]: '))
    idade = int(input(f'Informe a idade do {i + 1}° indivíduo: '))
    if (sexo == 'f' or sexo == 'F'):
        qtd_f += 1
        t_idade_f += idade
    elif (sexo == 'm' or sexo == 'M'):
        qtd_m += 1
        t_idade_m+= idade
med_idade_f = t_idade_f / qtd_f
med_idade_m = t_idade_m / qtd_m
print(f'A média de idade dos {qtd_f} mulheres é: {med_idade_f:} anos, enquato os {qtd_m} homens possuem ideade média de {med_idade_m} anos.')
