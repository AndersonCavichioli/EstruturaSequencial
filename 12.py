"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""

alt = float(input("Digite sua altura: "))

pesoIdeal = (72.7 * alt) - 58

print("Você tem {:.2f}m de altura e seu peso ideal é de {:.2f}kg" .format(alt, pesoIdeal))
