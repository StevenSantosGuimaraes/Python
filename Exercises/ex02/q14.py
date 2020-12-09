media_aprovacao = float(input("Informe a média necessária para aprovação no curso: "))
nome = str(input("Informe o nome do aluno(a): "))
sexo = str(input("Informe o sexo do aluno(a): "))
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media_final = (nota1 + nota2 + nota3) / 3

if media_final >= media_aprovacao:
    if sexo == 'm' or sexo == 'M':
        print(f"O aluno {nome} foi APROVADO com média {media_final:.2f} !!!")
    else:
        print(f"A aluna {nome} foi APROVADA com média {media_final:.2f} !!!")
else:
    if sexo == 'f' or sexo == 'F':
        print(f"A aluna {nome} foi REPROVADA com média {media_final:.2f} !!!")
    else:
        print(f"O aluno {nome} foi REPROVADO com média {media_final:.2f} !!!")
