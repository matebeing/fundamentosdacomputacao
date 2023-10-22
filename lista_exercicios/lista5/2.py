#Escrever uma função chamada DOBRA que multiplique um número inteiro
#recebido como parâmetro por 2. Escrever um programa para ler um valor
#inteiro e, utilizando a função DOBRA, calcular e exibir o dobro dele.

def dobra(num):
    return num * 2

n = int(input("Digite um número: "))
print(dobra(n))