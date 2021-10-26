"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math

m = float(input("Digite a área (em m²) a ser pintada: "))

a = m / 3 #Metragem dividido por 3, sendo que cada litro pinta 3 metros quadrados
b = 18 #Quantidade de litros por lata
d = a/b #Metragem dividido pela quantidade de litros da lata
c = math.ceil(d) #arredondamento pra mais da variavel C
vl = 80 #Valor lata
total = c * vl #Valor total

print("\nIrá precisar de: {} latas de {} litros (arredondado pra cima)" .format(c, b))
print("Cada lata custa: R${:.2f}" .format(vl))
print("Valor total a ser pago: R${:.2f}" .format(total))