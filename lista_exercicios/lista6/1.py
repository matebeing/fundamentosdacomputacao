# Escreva um programa que leia 10 números inteiros e armazene os positivos
# no vetor VETPOS e os negativos no vetor VETNEG. Ao final imprima os dois
# vetores.

vetor = [0] * 10

for i in range(len(vetor)):
    vetor[i] = int(input("Insert an integer number: "))


def splitNumbers(arr):
    VETPOS = [0] * 10
    VETNEG = [0] * 10

    for i in range(len(arr)):
        if arr[i] > 0:
            VETPOS[i] = arr[i]
        else:
            VETNEG[i] = arr[i]

    return VETPOS, VETNEG


print(splitNumbers(vetor))
