"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

f = float(input("Digite a temperatura em graus Fahrenheit: "))

c = f * (f-32) / 9

print("{:.2f}ºF é o equivalente a {:.2f}ºC" .format(f, c))