#Faça um programa que receba o peso e a altura de uma pessoa e calcule o índice de
#massa corpórea (IMC). Ele mede a relação entre peso e altura (peso em Kg, dividido
#pelo quadrado da altura em metros). O programa deve exibir o valor do IMC
#calculado.

weight = float(input("Insira o valor do peso: "))
height = float(input("Insira o valor da altura: "))

IMC = weight / height ** 2

print(IMC)