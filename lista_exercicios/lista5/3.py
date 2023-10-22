#Faça um programa que leia a medida de um raio e crie duas funções: uma
#para calcular a área do círculo e outra para calcular o perímetro da
#circunferência. Ao final, o programa deve exibir o resultado dos cálculos.

import math

radius = int(input("Digite a medida do raio: "))

while radius < 0:
    raio = int(input("Digite a medida do raio: (>= 0) "))

def circle_area(rad):
    return math.pi * math.pow(radius, 2)

def perimeter_circuference(rad):
    return 2 * (math.pi * radius)

area = circle_area(radius)
perimeter = perimeter_circuference(radius)

print(f'A área do círculo é {area} e o perímetro é {perimeter}')