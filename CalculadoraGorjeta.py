# Cumprimento e entrada

print("\nSeja bem-vindo(a) à calculadora de gorjeta da TipsCode.")

# Solicitação do valor total da conta

totalConta = float(input("\nPor favor, informe o valor total da sua conta: "))

# Perguntando o quanto gostaria de contribuir para a gorjeta

valorGorjeta = int(input("\nCerto, quanto você gostaria de contribuir em gorjeta, considere como porcentagem: 10, 12 ou 15: "))

# Perguntando quantas pessoas pagarão a conta

pessoasPagantes = int(input("\nQuantas pessoas pagarão a conta? "))

### Eu fui bem até aqui ^ Tive muita dificuldade para pensar no cálculo :((  Mas cheguei a seguinte conclusão:

# Cálculo total

gorjeta = (valorGorjeta / 100) * totalConta
totalComGorjeta = totalConta + gorjeta
totalPorPessoa = totalComGorjeta / pessoasPagantes


# Mensagem com o valor total a ser pago

print(f"\nO valor total a ser pago dividido por {pessoasPagantes} pessoas é de: R$ {totalPorPessoa:.2f}")


print("\nAgradecemos por usar nosso aplicativo :) ")






