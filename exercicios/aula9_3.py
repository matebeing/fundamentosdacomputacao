## Escreva um programa em Python que leia os catetos de um
## triangulo retângulo e calcule a hipotenusa. Exiba os dados ao
## final do programa.

opposite_side = int(input("Enter the value of the opposite side: "))
adjacent_side = int(input("Enter the value of the adjacent side: "))

hypotenuse = (opposite_side ** 2 + adjacent_side ** 2) ** (1/2)

print("The value of the hypotenuse is: ", hypotenuse)
