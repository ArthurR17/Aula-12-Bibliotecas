from string import *


senha = input("Digite uma senha: ")

if senha.isalnum() and not senha.isalpha() and not senha.isnumeric():
    print("Senha forte.")
else:
    print("Senha fraca.")

