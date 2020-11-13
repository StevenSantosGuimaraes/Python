def FatorialSemRecursividade(vlr):
    result = 1
    for i in range (1, vlr + 1):
        result *= i
    return (result)


def FatorialComRecursividade(vlr):
    if (vlr == 0):
        return (1)
    else:
        return (FatorialComRecursividade(vlr - 1) * vlr)

num = int(input("Informe um valor: "))
print(FatorialSemRecursividade(num))
print(FatorialComRecursividade(num))