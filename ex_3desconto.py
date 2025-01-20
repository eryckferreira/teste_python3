valorDaCompra = float(input("Qual foi o valor da compra: "))

if valorDaCompra > 200:
    desconto = 0.2
elif valorDaCompra > 100:
    desconto = 0.1
else:
    desconto = 0.05

valorFinal = valorDaCompra - (valorDaCompra * desconto)

print(f"O valor final com desconto é de R$ {valorFinal:.2f} ")