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
dados_cliente = {
    'Nome:': 'Maria',
    'Idade': '24',
    'Email': 'vaicomtudo@abc.com'
}

print(dados_cliente['Nome:'])

# Função que ordena lista
def ordList(l):
    pos = len(l)
    for i in range(pos):
        for j in range(1, pos - i):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]


aluno = {}
try:
    q = int(input("Digite quantos alunos serão avaliados: "))
except ValueError:
    print("[ERROR] O VALOR DEVE SER UM NÚMERO INTEIRO MAIOR QUE 0")
    q = int(input("Digite quantos alunos serão avaliados: "))

for c in range(1, q + 1):
    ok = False
    nome = ''
    while not ok:
        print("----------Cadastro {}º aluno-----------".format(c))
        nome = input(" Digite o nome do aluno: ")
        if (nome == '') or (nome.isnumeric()):
            print("\n---------[ERROR] campo vazio ou valor númerico encontrado!!---------\n")
            ok = False
            val = True
        else:
            ok = True

    # REINICIANDO AS VÁRIAVEIS
    nNotas = 1
    notas = []
    sNotas = 0
    somaDeNotas = 0
    listaDesor = []

    # RECEBENDO AS NOTAS DO ALUNO
    while nNotas <= 4:
        print("  Digite a {} nota do aluno".format(nNotas), end=' ')
        nota = int(input(' '))
        if (nota < 0) or (nota > 10):
            print("----------Valor de nota inválido!!----------")
            continue
        else:
            notas.append(nota)
            listaDesor.append(nota)
            nNotas += 1
    ordList(notas)
    notas.remove(notas[0])
    for v in listaDesor:
        if v not in notas:
            listaDesor.remove(v)

    for notaV in notas:
        somaDeNotas += notaV

    media = somaDeNotas / 3

    # TIRANDO A MÉDIA
    if media >= 6:
        result = 'Aprovado'
    else:
        result = 'Reprovado'

    aluno[nome] = (listaDesor, media, result)
    print("\n\n")

print("|--------------------------Resultados--------------------------|")
for user, dados in aluno.items():
    print("                         Nome: {}".format(user))
    print("                          Notas: {}".format(dados[0]))
    print("                          Media: {:.1f}".format(dados[1]))
    print("                          Rsultado: {}".format(dados[2]))
print("-----------------------Fim Resultados-----------------------|")
