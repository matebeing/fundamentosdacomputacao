#Elabore um programa que leia uma temperatura em graus Fahrenheit e faça
#uma função que receba esse valor informado e converta de graus Fahrenheit
#para graus centígrados.

def fahrenheit_to_celsius(f):
   return 5/9 * (f - 32)

f = float(input("Digite a temperatura em Fahrenheit: "))
print("A temperatura em Celsius é: ", fahrenheit_to_celsius(f))