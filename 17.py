"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
A - comprar apenas latas de 18 litros;
B - comprar apenas galões de 3,6 litros;
C - misturar latas e galões, de forma que o desperdício de tinta seja menor e sempre arredonde os valores para cima, isto é, considere latas cheias."""


from math import ceil, floor

#leitura da area total
tamanho = float(input("Digite a área (em m²) a ser pintada: "))

#declaração das variaveis
litro = tamanho / 6
latas = litro / 18
galoes = litro / 3.6
latas_arredondado = ceil(latas) #arredonda pra cima
galoes_arredondado = ceil(galoes)

latas_baixo = floor(latas) #areredonda pra baixo
latas_subtrair = latas_baixo * 18
resto = litro - latas_subtrair
galoes_resto = resto / 3.6
galoes_resto_arredondado = ceil(galoes_resto)
preco_galao_resto = galoes_resto_arredondado * 25
preco_lata_baixo = latas_baixo * 80
preco_total_misturado = preco_lata_baixo + preco_galao_resto

preco_lata = latas_arredondado * 80
preco_galao = galoes_arredondado * 25


print("\nQuantidade de latas: {}, valor: R${:.2f} " .format(latas_arredondado, preco_lata))
print("Quantidade de galões: {}, valor: R${:.2f} " .format(galoes_arredondado, preco_galao))
print("\nMisturando latas e galões:")
print("Quantidade de latas: {}".format(latas_baixo))
print("Quantidade de galoes: {}" .format(galoes_resto_arredondado))
print("Preço total misturado: R${:.2f}" .format(preco_total_misturado))

#estrutura de decisao não pedido no enunciado mas mostra entre as 3, qual a melhor vantagem
if preco_total_misturado < preco_lata and preco_total_misturado < preco_galao:
    print("\n--> Vantagem: mistirar latas e galões")

elif preco_lata < preco_total_misturado and preco_lata < preco_galao:
    print("--> Vantagem: comprar somente latas")

else:
    print("--> Vantagem: comprar somente galões")

