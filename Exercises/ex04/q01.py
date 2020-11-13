# Escreva uma função que recebe um número inteiro como parãmetro de entrada e retona o texto "PAR" ou "ÍMPAR".

def ParImpar(num):
    if num % 2 == 1:
        msg = "IMPAR."
        return msg
    else:
        msg = "PAR."
        return msg

X = int(input("Informe um número: "))
res = ParImpar(X)
print("O número informado foi {0} e ele é: {1} !!!".format(X, res))