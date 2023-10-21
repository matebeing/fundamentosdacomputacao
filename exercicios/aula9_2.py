# Escreva um programa em Python para ler o número total de eleitores
# de um município, o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação
# ao total de eleitores.

eleitores = int(input("Digite o número de eleitores: "));

votosBrancos = int(input("Digite o número de votos brancos: "));
votosNulos = int(input("Digite o número de votos nulos: "));
votosValidos = int(input("Digite o número de votos válidos: "));

percentualBrancos = (votosBrancos / eleitores) * 100;
percentualNulos = (votosNulos / eleitores) * 100;
percentualValidos = (votosValidos / eleitores) * 100;

print("Percentual de votos brancos: ", percentualBrancos);
print("Percentual de votos nulos: ", percentualNulos);
print("Percentual de votos válidos: ", percentualValidos);