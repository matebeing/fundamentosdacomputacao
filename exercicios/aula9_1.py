# Faça um programa em Python que solicite que o usuário informe as
# medidas correspondentes aos lados de um retângulo, calcule a área e
# perímetro desse retângulo e exiba todos esses dados.

width = int(input("Insert the width of the rectangle: "))
height = int(input("Insert the height of the rectangle: "))

area = width * height;
perimeter = 2 * (width + height);

print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)