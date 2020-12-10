qtd_ler = int(input('Quantos valores deseja ler? '))
maior_idade, idade, i = 0, 0, 0
maior_nome, nome = '', ''
while i < qtd_ler:
    nome = str(input(f'Informe o nome da {i + 1}º pessoa: '))
    idade = int(input(f'Informe a idade de {nome}: '))
    if idade > maior_idade:
        maior_idade = idade
        maior_nome = nome
        i += 1
    else:
        i += 1
print(f'A pessoa mais velha é {maior_nome} e sua idade é {maior_idade}.')
