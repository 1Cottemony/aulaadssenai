class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura)/2

firnas = [Retangulo(10,5), Triangulo(10,5)]
for forma in formas:
    print("Área", forma.area())