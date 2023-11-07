from datetime import date


ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
idade = date.today().year - ano
idade_mes = date.today().month - mes


if idade_mes < 0:
    idade_mes = 12 + idade_mes
    idade -= 1


print(f"Você tem {idade} anos e {idade_mes} meses.")