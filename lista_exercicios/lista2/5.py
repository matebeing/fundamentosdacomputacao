# Elabore um programa que leia uma quantidade de segundos e transforme este
# tempo em dias, horas e minutos. Ao final, o programa deve exibir essas informações.

seconds = int(input("Digite a quantidade de segundos"))

print(f'Dias {seconds / 86400}, horas {seconds / 3600}, minutos {seconds / 60}')