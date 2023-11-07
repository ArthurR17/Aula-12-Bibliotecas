import random

tentativas = 3

while tentativas > 0:
    print(f"Você tem {tentativas} tentativas.")
    numero_secreto = random.randint(1, 10)
    numero_usuario = int(input("Digite um número: "))
    if numero_usuario == numero_secreto:
        print("Você acertou!")
        break
    elif numero_usuario > numero_secreto:
        print("O número secreto é menor.")
        tentativas -= 1
    elif numero_usuario < numero_secreto:
        print("O número secreto é maior.")
        tentativas -= 1
