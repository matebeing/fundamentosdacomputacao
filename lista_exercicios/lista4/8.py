# Considere um pais  A com 5.000.000 habitantes e uma taxa de
# natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e
# uma taxa de natalidade de 2% ao ano. Faça um programa que calcule e
# imprima o tempo necessário para que a população do país A ultrapasse a
# população do país B.

paisA = 5000000
paisB = 7000000
anos = 0

while (paisA < paisB):  # while True > while False

    anos += 1

    paisA = paisA + (0.3 * paisA)
    paisB = paisB + (0.2 * paisB)

print(anos)
# while condição:  ## "rosa" == "rosa" = True "laranja" == "abacate" = False
# corpo
