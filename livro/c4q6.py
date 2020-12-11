n1 = int(input('Informe o primeiro termo: '))
n2 = int(input('Informe a razão: '))
n3 = int(input('Informe a quantidade de termos: '))
lista = []
print(lista)
i = 1
while i < n3:
    num = lista[i - 1] + n2
    lista.append(num)
    i += 1
print(lista)
