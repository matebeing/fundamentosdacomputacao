x = int(input("Informe o primeiro valor: "))
y = int(input("Informe o segundo valor: "))
operation = int(input("Escolha uma das seguintes operações: \n 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n\n >> "))

match operation:
	case 1:
		print(x + y)
	case 2:
		print(x - y)
	case 3:
		if y != 0:
			print(x / y)
		else:
			print("Não é possível dividir " + str(x) + " por 0")
	case 4: 
		print(x * y)
	case _:
		print("Operação inválida.")

