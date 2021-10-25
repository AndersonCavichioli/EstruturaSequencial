"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

#pede a entrada do raio
r = float(input("Digite o raio: "))

#valor do pi (4 casas decimais)
pi = 3.1415

#cálculo da área
area = pi*(r ** 2)

#imprime o resultado
print("A área do círculo é: {:.2f}" .format(area))