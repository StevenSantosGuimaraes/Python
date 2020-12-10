qtd_registros = int(input('Quantos registros devo realizar? '))
idade, med_idade_f, med_idade_m, t_idade_f, t_idade_m = 0, 0, 0, 0, 0
qtd_m, qtd_f, i = 0, 0, 0
sexo = ''
while i < qtd_registros:
    sexo = str(input(f'Informe o sexo do {i+1}° indivíduo [F/M]: '))
    idade = int(input(f'Informe a idade do {i + 1}° indivíduo: '))
    if sexo == 'f' or sexo == 'F':
        qtd_f += 1
        t_idade_f += idade
        i += 1
    elif sexo == 'm' or sexo == 'M':
        qtd_m += 1
        t_idade_m += idade
        i += 1
med_idade_f = t_idade_f / qtd_f
med_idade_m = t_idade_m / qtd_m
print(f'A média de idade de(as) {qtd_f} mulher(es) é: {med_idade_f:.0f} anos, enquato o(s) {qtd_m} homem(ns) possuem ideade média de {med_idade_m:.0f} anos.')
