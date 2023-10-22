#Elaborar um programa que solicita a entrada de 3 valores (a, b, c) e verifica se esses
#valores podem formar ou não um triângulo. Você deve considerar que os valores
#lidos são inteiros e positivos. Caso os valores formem um triângulo, exiba essa
#informação e o valor do perímetro deste triângulo. Se não formarem triângulo,
#apenas exiba uma mensagem com essa informação. (Obs.: Para formar um triângulo,
#cada suposto lado deve ser menor do que a soma dos outros dois lados.)

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if (a < (b + c)):
    print("Os valores formam um triângulo.")
    print("O perímetro do triângulo é: ", (a + b + c))
elif (b < (a + c)):
    print("Os valores formam um triângulo.")
    print("O perímetro do triângulo é: ", (a + b + c))
elif (c < (a + b)):
    print("Os valores formam um triângulo.")
    print("O perímetro do triângulo é: ", (a + b + c))
else:
    print("Obs.: Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados.")
