pessoa1 = str(input("Informe o nome da primeira pessoa: "))
peso1 = float(input("Informe o peso da primeira pessoa: "))
pessoa2 = str(input("Informe o nome da segunda pessoa: "))
peso2 = float(input("Informe o peso da segunda pessoa: "))

if peso1 > peso2:
    print(f"{pessoa1} é mais pesado(a) que {pessoa2} !!!")
elif peso1 < peso2:
    print(f"{pessoa2} é mais pesado(a) que {pessoa1} !!!")
