def par_impar(num):
    if num % 2 == 0:
        msg = "PAR!"
        return msg
    else:
        msg = "ÍMPAR!"
        return msg


x = int(input("Informe um número: "))
res = par_impar(x)
print(f'O número informado foi {x} e ele é: {res}')
