#Elabore um programa que leia a medida de um raio de um círculo e efetue o cálculo
#da sua área, exibindo o resultado ao final

radius = int(input("Insira a medida do raio do círculo: "))

while radius < 0:
    radius = int(input("Insira a medida do raio do círculo: (> 0) "))

print(3.14 * radius ** 2)