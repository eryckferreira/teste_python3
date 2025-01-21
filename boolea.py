# Variaveis
nomeLimpo = True

# Pergunta ao usuário
resposta = input("Sua renda está acima de R$ 5.000? Escreva 'sim' ou 'nao': ")

# Avaliação da resposta
if resposta == "sim":
    rendaAcima5Mil = True
elif resposta == "nao":
    rendaAcima5Mil = False
else:
    print("Resposta inválida")
    rendaAcima5Mil = None

# Verificação da Aprovação do financiamento
if rendaAcima5Mil and nomeLimpo:
    print('financiamento aprovado!')
else:
    print("financiamento negado")
