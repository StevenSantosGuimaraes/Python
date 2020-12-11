import random
i, n, y = 1, 0, 0
lista_v = []
while i == 1:
    n = int(input('Informe um valor entre 0 e 50: '))
    if 0 <= n <= 50:
        a = 1
        while a <= n:
            lista_v.append(random.randint(-10, 10))
            if lista_v.count(y) != 0:
                lista_v.remove(y)
            else:
                a += 1
        print(lista_v)
        i = 0
    else:
        print(f'Valor {n} não obedece o critério. Favor informe um valor válido.')
while i < n:
    if len(lista_v) > 0:
        x = int(input(f'Restam {len(lista_v)} itens, qual valor devo buscar e eliminar? '))
    else:
        x = 0
    teste = lista_v.count(x)
    if x == 0 or teste == 0:
        i = n
        print('Programa encerrado!')
    else:
        if teste != 0:
            while teste != 0:
                lista_v.remove(x)
                teste = lista_v.count(x)
        else:
            print(f'O valor informado {x} não está na lista, informe outro número ou 0 para encerrar o programa.')
