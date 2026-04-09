#Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.
dicionario = {}
def inserirDados():
    while True:
        try:
            valora = input(f"Digite o valora: ")
            if valora == "":
                break
            valorb = int(input(f"Digite o valorb: "))
            dicionario[valora] = valorb
            print(dicionario)
        except:
            print("Insira um valor válido da próxima vez")
inserirDados()
resultado = max(dicionario, key=dicionario.get)
print("O maior valor é: ", resultado,dicionario.get(resultado))

