a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

if b < a:
    for i in range(b, a):
        print(i)
elif b > a:
    for i in range(a, b +1):
        print(i)
