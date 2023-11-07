from math import cos, sin, tan, radians


angulo = float(input("Digite o ângulo: "))

print(f"O seno do ângulo é: {sin(radians(angulo)):.2f}")
print(f"O cosseno do ângulo é: {cos(radians(angulo)):.2f}")
print(f"A tangente do ângulo é: {tan(radians(angulo)):.2f}")


