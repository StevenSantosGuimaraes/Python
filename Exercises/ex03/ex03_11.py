listagem = []
soma = 0
tamanho = int(input('Quantidade de números a serem lidos: '))
for contador in range(0, tamanho):
    novoNum = int(input('Digite um número: '))
    soma += novoNum
else:
    media = (soma / tamanho)
    print("A soma dos números informados é:", soma, "e a média:", media)