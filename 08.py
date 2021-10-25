"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

#solicitação das entradas
vh = float(input("Qual valor ganho por hora: "))
hm = int(input("Quantas horas trabalhadas no mes: "))

#cálculo do salario mês
salario = vh * hm

print("O salário do mês é: R${:.2f}" .format(salario))

