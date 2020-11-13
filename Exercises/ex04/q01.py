def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

x = int(input("Informe qual número fibonacci deseja ver: "))
res = fibonacci(x - 1)
print("O fibonacci de %d é %d" % (x, res))