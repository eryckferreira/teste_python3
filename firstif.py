idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade!")
elif idade >= 18 and idade <= 60:
    print("Você é um Adulto!")
else:
    print("Idoso!")
2