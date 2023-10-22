# Um comerciante calcula o valor da venda de produtos, com base na tabela abaixo:

valorAtual = float(input("Digite o valor do produto: "))
valorFinal = 0

if valorAtual < 20:
    valorFinal = valorAtual * 0.70
elif valorAtual >= 20 and valorAtual <= 50:
    valorFinal = valorAtual * 0.50
elif valorAtual >= 50 and valorAtual <= 100:
    valorFinal = valorAtual * 0.40
else:
    valorFinal = valorAtual * 0.30

print("Valor final: R$ %.2f" % (valorFinal + valorAtual))
