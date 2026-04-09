#Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.
dicionario = {}
def inserirDados():
    while True:
        try:
            valora = input(f"Digite o Nome: ")
            if valora == "":
                break
            valorb = int(input(f"Digite a Idade: "))
            dicionario[valora] = valorb
            print(dicionario)
        except:
            print("Insira um valor válido da próxima vez")

def filtrar_maiores(dicionario):
    