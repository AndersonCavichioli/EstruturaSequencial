"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

c = float(input("Digite a temperatura em ºC: "))

f = (c * (9/5)) + 32

print("{}ºC é igual a {}ºF" .format(c, f))
