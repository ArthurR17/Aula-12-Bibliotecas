from math import log
from math import *

base = int(input("Digite a base do logaritmo: "))
numero = int(input("Digite o número do logaritmo: "))
logaritmo = log(numero, base)

print(f"O logaritmo de {numero} na base {base} é: {logaritmo:.2f}")

