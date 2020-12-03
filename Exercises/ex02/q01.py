"""
Lista em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também podemos colocar QUALQUER tipo de dado.
"""
lista1 = list(range(10))
print(lista1)
lista2 = list(range(3))
print(lista2)
lista1.append(lista2)
print(lista1)
lista1.extend(lista2)
print(lista1)
print(lista1[-4][-1])
lista1.pop(-2)
print(lista1)
lista3 = ['Programação', 'em', 'Python']
print(lista3)
curso = ' '.join(lista3)
print(curso)
