tipo = input("Digite par ou impar: ")
for i in range(1, 101):
    if tipo == "par" and i % 2 == 0:
        print("O valor", i, "é par")
    elif tipo == "impar" and 1 % 2 != 0:
        print("o valor", i, "é impar")
    else:
        print("Entre com o tipo correto!")