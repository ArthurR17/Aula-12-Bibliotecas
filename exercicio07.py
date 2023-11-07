import datetime
from datetime import date

dia1 = input("Digite um dia com o formato (DD-MM-AAAA): ")
dia2 = input("Digite outro dia com o formato (DD-MM-AAAA): ")

dia1 = datetime.datetime.strptime(dia1, "%d-%m-%Y")
dia2 = datetime.datetime.strptime(dia2, "%d-%m-%Y")

diferenca = dia1 - dia2

print(f"A diferença entre as datas é de {abs(diferenca.days)} dias.")
