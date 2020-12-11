lista = []
res = 'n'
i, num = 0, 0
while res != 's' or res != 'S':
    num = int(input(f'Informe o {i + 1}° valor: '))
    lista.append(num)
    res = str(input('Deseja sair? [Sim/Não] '))
    if res == 'n' or 'N':
        i += 1

print(lista)
