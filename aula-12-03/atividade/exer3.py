s = n1 = 0

print("Digite números inteiros para somar.")
print("Um número negativo encerrará o programa.")

while n1 >= 0:
    n1 = int(input("Digite uma sequencia de numeros inteiros: "))
    s += n1
    print(s)