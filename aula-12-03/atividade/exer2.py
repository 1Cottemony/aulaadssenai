import random
numero_secreto = random.randint(1, 100)
print("Tente adivinhar o número secreto!")
chute = int(input("Insira o seu chute: "))

while chute != numero_secreto:
    if chute > numero_secreto:
       chute = int(input("O seu chute é maior que o número secreto! Tente novamente: "))
    elif chute < numero_secreto:
       chute = int(input("O seu chute é menor que o número secreto! Tente novamente: "))
    
print("Parabéns, você acertou!")