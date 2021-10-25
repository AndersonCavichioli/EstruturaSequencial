"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A - o produto do dobro do primeiro com metade do segundo .
B - a soma do triplo do primeiro com o terceiro.
C - o terceiro elevado ao cubo."""

#leitura dos numeros
n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
n3 = int(input("Digite n3: "))

print("\n01 - o produto do dobro do primeiro com metade do segundo ")

#cálculo A
a = (n1*2)*2 + (n2/2)
print(a, "\n")

print("a soma do triplo do primeiro com o terceiro ")

#cálculo B
b = (n1*3) + n3
print(b, "\n")

print("o terceiro elevado ao cubo")

#cálculo C
c = n3 ** 3

print(c)

