n = int(input('Insira um valor entre 1 e 45: '))
fib_list = [ ]
f1 = 0
f2 = 1

if n == 0 or n > 45:
  pass
else:
  for i in range(n):
    f3 = f2 + f1
    f2 = f1
    f1 = f3
    fib_list.append(str(f2))

    fib_string = ' '.join(fib_list)
  print(fib_string)