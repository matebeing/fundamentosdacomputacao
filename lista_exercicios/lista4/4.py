#Escreva um programa que imprima todos os números pares
#compreendidos entre 85 a 907. O algoritmo deve também calcular a
#soma destes valores.

sum = 0

for i in range(84, 907):
    if i % 2 == 0:
        sum += i
        print(i, sum)