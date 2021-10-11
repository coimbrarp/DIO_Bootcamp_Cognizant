x = float(input('Insira um valor: '))

for i in range(100):
    print("N[{}] = {:.4f}".format(i, x))
    x /= 2