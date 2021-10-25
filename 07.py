"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""

#leitura dos lados do quadrado
a = float(input("Digite lado a: "))
b = float(input("Digite lado b: "))

#cálculo da area do quadrado
area = a*b

#mostrar o resultado da área e o seu drobro
print("A área do quadrado é: {}" .format(area))
print("O dobro de {} é: {}" .format(area, area*2))
