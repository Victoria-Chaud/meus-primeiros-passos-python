# Escreva um programa que calcula o Índice de Massa Corporal de alguém, usando o peso e a altura do usuário.

# Link usado para entender sobre o IMC: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal

# Cumprimento:

print("Olá, vamos calcular o seu Índice de Massa Corporal (IMC)?")

# Usuário fornece os dados:

peso = float(input("Por favor, digite o seu peso em Kg (ex.: 70.5): "))

altura = float(input("Agora digite sua altura em metros (ex.: 1.75): "))

# Cálculo de IMC

imc = peso / (altura **2)

# Análise do resultado conforme tabela apresentada no link acima. O resultado será arredondado por "round":

print("\nSeu IMC é de: ", round(imc, 2))

if imc < 17: 
    print("Situação: Muito abaixo do peso.")
elif imc >= 17 and imc <= 18.49:
    print("Situação: Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.99:
    print("Situação: Peso normal.")
elif imc >= 25 and imc <= 29.99:
    print("Situação: Acima do peso.")
elif imc >= 30 and imc <= 34.99:
    print("Situação: Obesidade I.")
elif imc >= 35 and imc <= 39.99:
    print("Situação: Obesidade II")
else: # imc >= 40
    print("Situação: Obesidade III (mórbida).")