# Analise as seguintes regras para o cálculo do imposto de renda, de acordo com a
# renda mensal de um indivíduo:

#Renda mensal até R$ 1.903,98: Isento de imposto de renda
#• Renda mensal de R$ 1.903,99 a R$ 2.826,65: 7,5% de imposto de renda
#• Renda mensal de R$ 2.826,66 a R$ 3.751,05: 15% de imposto de renda
#• Renda mensal de R$ 3.751,06 a R$ 4.664,68: 22,5% de imposto de renda
#• Renda mensal superior a R$ 4.664,68: 27,5% de imposto de renda
#• Com base nessas regras, escreva um programa que calcule o imposto de renda a partir
#da renda mensal informada pelo usuário. Ao final, o programa deve exibir o salário bruto
#informado e o valor a ser pago de imposto.


renda = int(input("Digite sua renda mensal: "))

imposto = 0

if renda <= 1903.98:
    print("Isento de imposto de renda")
elif renda >= 1903.99 and renda <= 2826.65:
    imposto = renda * 0.075
elif renda >= 2826.66 and renda <= 3751.05:
    imposto = renda * 0.15
elif renda >= 3751.06 and renda <= 4664.68:
    imposto = renda * 0.225
else:
    imposto = renda * 0.275

salarioBruto = renda - imposto

print("Salário bruto: R$ %.2f, imposto a ser pago R$ %.2f" % (salarioBruto, imposto))

