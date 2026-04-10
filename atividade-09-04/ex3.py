class Calculadora:
    def adicionar(self, a,b):
        return a+b
    def subtrair(self, a,b):
        return a-b
    def multiplicar(self, a,b):
        return a*b
    def dividir(self, a,b):
        if b == 0:
            return("n pode dividir por 0, irmão do Jorel!!")
        return a/b

calc = Calculadora()
print(calc.adicionar(10,5))
print(calc.subtrair(10,5))
print(calc.multiplicar(10,5))
print(calc.dividir(10,5))