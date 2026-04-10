class pessoa:
    def __init__(self, nome, idade): #função construtora
        if nome is None:
            nome = input("Digite seu nome: ")
        if idade is None:
            idade = int(input("Digite a sua idade: "))
        
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print("Olá", self.nome)
        print("Você tem:", self.idade, "anos")
    
pessoa1 = pessoa()
pessoa1.apresentar()
aluna = pessoa("Ana", 21)
aluna.apresentar()