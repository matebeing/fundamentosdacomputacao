#Faça um programa que leia dois pontos de um plano cartesiano, P1(x1, y1) e
#P2(x2, y2) e calcule e exiba a distância entre eles. Esta distância deve ser
#calculada por meio de uma função desenvolvida por você. A fórmula que
#efetua esse cálculo é:
import math

# P1(X, Y)
PX1 = int(input("Insira o valor do eixo X do P1: "))
PY1 = int(input("Insira o valor do eixo Y do P1: "))

print(f'P1({PX1}, {PY1})')

# P2(X, Y)
PX2 = int(input("Insira o valor do eixo X do P2: "))
PY2 = int(input("Insira o valor do eixo Y do P2: "))

print(f'P2({PX2}, {PY2})')


def distance(x, y, x2, y2):
    return math.sqrt(math.pow((x - x2), 2) + math.pow((y - y2), 2))
    

distance = distance(PX1, PY1, PX2, PY2);


print(distance)