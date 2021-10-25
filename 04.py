"""Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

#leitura das notas
n1 = float(input("Digite a nota do 1 bimestre: "))
n2 = float(input("Digite a nota do 2 bimestre: "))
n3 = float(input("Digite a nota do 3 bimestre: "))
n4 = float(input("Digite a nota do 4 bimestre: "))

#cálculo da média
media = (n1+n2+n3+n4) / 4

#mostrar a média na tela
print("A média das notas dos bimestres é: {:.2f}" .format(media))