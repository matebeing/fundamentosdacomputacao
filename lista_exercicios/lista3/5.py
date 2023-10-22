#Faça um programa que leia três números inteiros e exiba o maior valor informado.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if (a > b) and (a > c):
    print("O maior valor é: ", a)
elif (b > a) and (b > c):
    print("O maior valor é: ", b)
else:  
    print("O maior valor é: ", c)
    