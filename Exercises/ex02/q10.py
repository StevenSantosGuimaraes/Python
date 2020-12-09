nota1 = float(input("Informe a primeira nota: ")) * 0.2
nota2 = float(input("Informe a segunda nota: ")) * 0.3
nota3 = float(input("Informe a terceira nota: ")) * 0.5
media_final = nota1 + nota2 + nota3

if media_final >= 6.0:
    print("Aluno APROVADO !!!")
else:
    print("Aluno REPROVADO !!!")
