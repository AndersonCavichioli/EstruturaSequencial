"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
A - Para homens: (72.7*h) - 58
B - Para mulheres: (62.1*h) - 44.7"""

#captura da altura da pessoa
h = float(input("Digite sua altrura: "))

#cálculo para homens e mulheres
a = (72.7*h) - 58
b = (62.1*h) - 44.7

#saída do resultado para ambos os sexos
print("o peso ideal para homem com essa altura: {:.2f}kg" .format(a))
print("o peso ideal para mulher com essa altura: {:.2f}kg" .format(b))
