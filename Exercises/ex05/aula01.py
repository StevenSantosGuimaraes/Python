# Listas e tuplas são conjunto de dados, com diferença onde a Lista [] são multáveis e tuplas () são imutárveis.

lista = ['Java', 'C', 'Pascal', 'Python', 'Cobol']
tupla = ('Java', 'C', 'Pascal', 'Python', 'Cobol')
print(lista)
print(tupla)
print(type(lista))
print(type(tupla))
lista[1] = 'C++'
# tupla[1] = 'C++' // Objeto imutável
print(lista)
print(tupla[2]) # Indice cresce a partir de ZERO
print(tupla[-2]) # Indice decresce a partir de MENOS UM
print(len(lista))
lista.append('Basic')
print(lista)
print(lista[1:4+1])
print(len(tupla))