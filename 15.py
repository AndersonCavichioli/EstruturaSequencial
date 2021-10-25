"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
A - salário bruto.
B - quanto pagou ao INSS.
C - quanto pagou ao sindicato.
D - o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

#captura valor hora e horas trabalhadas
vh = float(input("Digite o valor hora: "))
ht = int(input("Digite as horas trabalhadas: "))

#calcula os impostos, sb e sl
sb = vh * ht
ir = sb * 0.11
inss = sb * 0.08
sindicato = sb * 0.05

sl = sb - ir - inss - sindicato

print("Salario bruto: R${:.2f}" .format(sb))
print("Imposto de renda (11%): R${:.2f}" .format(ir))
print("INSS (8%): R${:.2f}" .format(inss))
print("Sindicato (5%): R${:.2f}" .format(sindicato))
print("Salario liquido: R${:.2f}" .format(sl))
