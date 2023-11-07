from math import sqrt as raiz

c1 = int(input("Digite a medida do cateto oposto: "))
c2 = int(input("Digite a medida do cateto adjacente: "))

h = raiz(c1 ** 2 + c2 ** 2)

print(f"A medida da hipotenusa é: {h}")
