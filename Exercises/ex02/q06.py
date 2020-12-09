num = int(input("Informe um número: "))
multiplo = int(input("Informe o multiplo desejado: "))
teste = num % multiplo

if teste == 0:
    print(f"O número {num} é multiplo de {multiplo} !!!")
else:
    print(f"O número {num} não é multiplo de {multiplo} !!!")
