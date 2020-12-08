salario = float(input("Informe o salário do vendedor: "))
vendas = float(input("Informe o total vendido no mês: "))
percentual = float(input("Informe o percentual de comissão do vendedor: "))
percentual /= 100
valor_final = salario + vendas * percentual
print(f"O valor final a pagar é: {valor_final:.2f}")
