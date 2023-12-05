# Elabore um programa que leia 10 números inteiros em um vetor e
# imprima-os na ordem inversa.

vetor = [0] * 10

for i in range(len(vetor)):
    vetor[i] = int(input("Insert a number: "))


def inverse(array):
    inverseArray = [0] * 10
    for i in range(len(array)):
        print(array[len(array) - i])

 #   return inverseArray, array


inverse(vetor)
# print(inverse(vetor))
