#A confederação brasileira de natação irá promover eliminatórias para o próximo
#mundial. Faça um programa que leia a idade de um nadador e exiba a sua categoria
#de acordo com a seguinte tabela:

age = int(input("Digite sua idade: "))

if age < 5:
    print("Não pode participar")
elif age >= 5 and age <= 7:
    print("Infantil A")
elif age >= 8 and age <= 10:
    print("Infantil B")
elif age >= 11 and age <= 13:
    print("Juvenil A")
elif age >= 14 and age <= 17:
    print("Juvenil B")
else:
    print("Sênior")
